#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: michael


Class for time series analysis for different poses estimates 
for robot localisation.
"""

import pandas as pd
import numpy as np
from dateutil import parser
from datetime import timezone,datetime
import statistics

class Odometry:
    def __init__(self,ground_truth,Odometrydataframe):
        self.ground_truth = pd.read_csv(ground_truth)
        self.Odometrydataframe = pd.read_csv(Odometrydataframe)
        self.initial_time = self.ground_truth.loc[0,'time']
    
    """
    There a control dataframe will be created so as to compare
    with the test dataframe. Since, in most cases, the time headers
    are not synchronised and are not of same length, an interpolation 
    will be done;
    
    1. The time headers from the test dataframe and train dataframe will be extracted.
    2. Both will be convert to epoch time then compiled together, then they will be sorted
    3. For each dataframe the various rows will be indexed based on their respective epoch time
    4. Then for the control dataframe(ground truth) the data was interpolated, for the train dataframe,
       the Nan values were filled with zeroes so as not to temper with the data.

    """
    def interpolate(self,base):
        def synchronisation(base,top,padding_method):
            def utc_time(dataframe):
                
                initial_time = datetime.strptime(self.initial_time, '%Y/%m/%d/%H:%M:%S.%f')
                
                for index,series in dataframe.iterrows():
                    time_frame = datetime.strptime(series["time"], '%Y/%m/%d/%H:%M:%S.%f')
                    elapsed_time = time_frame.replace(tzinfo = timezone.utc).timestamp() - initial_time.replace(tzinfo = timezone.utc).timestamp() 
                    
                    dataframe.loc[index,'time'] = elapsed_time
                return dataframe
            
            control = utc_time(base)
            target = utc_time(top)
            for __,series in target.iterrows():
                control = control.append({"time":series["time"]},ignore_index = True)
            if padding_method == 'Linear':
                control = control.sort_values(by=['time']).interpolate(method='linear',
                                                                       limit_direction='forward',
                                                                       axis = 0)
            else:
                control = control.sort_values(by=['time']).fillna(0)
            return control
        
        if base == 'control':
            dataframe = synchronisation(self.ground_truth,self.Odometrydataframe,'Linear')
        elif base =='target':
            dataframe = synchronisation(self.Odometrydataframe,self.ground_truth,None)
        return dataframe
    

    def data_extraction(self,control,target,covariance_steps):
        array_of_x = []
        array_of_y = []
        base_x = []
        base_y = []
        test_x = []
        test_y = []
        
        for index,series in target.iterrows():
            if series[".pose.pose.position.x"] == 0 and series[".pose.pose.position.y"] == 0:
                pass
            else:
                delta_X = abs(series[".pose.pose.position.x"]-control.iloc[index][".pose.pose.position.x"])
                delta_Y = abs(series[".pose.pose.position.y"]-control.iloc[index][".pose.pose.position.y"])
                
                array_of_x.append(delta_X)
                array_of_y.append(delta_Y)
                
                base_x.append(control.iloc[index][".pose.pose.position.x"])
                base_y.append(control.iloc[index][".pose.pose.position.y"])
                
                test_x.append(series[".pose.pose.position.x"])
                test_y.append((series[".pose.pose.position.y"]))
        
        steps = covariance_steps
        
        def covariance(steps,control_list,target_list):
            
            sliced_list_base_x = [[control_list[i:i+steps]] for i in range(0, len(control_list), steps)]
            sliced_list_test_x = [[target_list[i:i+steps]] for i in range(0, len(target_list), steps)]
            
            covariance_array_x = []
           
            for index,elements in enumerate(sliced_list_base_x):
                covariance_array_x.append(np.cov(elements,sliced_list_test_x[index]))
                
            return covariance_array_x
        
        
        return array_of_x, array_of_y ,covariance(steps,base_x,test_x),covariance(steps,base_y,test_y)

    

"""
Example Code below, you only have to replace
for the csv path below;

Here the analysis was between visual odometry and ground truth.

"""

ground_truth = './corridordiffbot_odom.csv'
train_dataframe = './corridorvisual_odom.csv'

analysis = Odometry(ground_truth, train_dataframe)

control = Odometry(ground_truth, train_dataframe).interpolate('control')
target = Odometry(ground_truth, train_dataframe).interpolate('target')

deviation_of_X, deviation_of_Y,covariance_array_of_X,covariance_array_of_Y = analysis.data_extraction(control,target,4)

#Data analysis for x-component
mean_deviation_of_X = statistics.mean(deviation_of_X)
standard_deviation_of_X = statistics.stdev(deviation_of_X)
variance_of_X = statistics.variance(deviation_of_X)


#Data analysis for y-component
mean_deviation_of_Y = statistics.mean(deviation_of_Y)
standard_deviation_of_Y = statistics.stdev(deviation_of_Y)
variance_of_Y = statistics.variance(deviation_of_Y)

print(covariance_array_of_Y)
