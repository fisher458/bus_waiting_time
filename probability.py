import pandas as pd
import config

import math
import numpy as np
file = config.file
from scipy.stats import skew



def detect(stop_name, direction=0,wait_time = 3,start_point=0):
    df = pd.read_csv(file)
    leave_time = []
    time_list = []
    estimate_time_list = []
    e = 0
    filter_condition = (df['StopName'] == stop_name) & \
                       (df['Direction'] == direction)
    
    df_filtered = df[filter_condition]
    for i in range(start_point-1,len(df_filtered)-1):
        data_g = df_filtered.iloc[i]['EstimateTime']
        data_h = df_filtered.iloc[i+1]['EstimateTime'] 
        if data_h - data_g > 0 : #啥時開走
            leave_time.append(i)
        elif int(math.ceil(data_g)) == wait_time : #預估時間
            estimate_time_list.append(i)
    
    
    for idx in estimate_time_list:
        leave_time_array = np.array(leave_time)
        index = np.searchsorted(leave_time_array,idx)
        number = leave_time[index]
        time_data_g = df_filtered.iloc[idx]['SrcUpdateTime'] 
        time_data_h = df_filtered.iloc[number]['SrcUpdateTime']
        time_gap = pd.to_datetime(time_data_g) - pd.to_datetime(time_data_h)
        
        time_gap_halfmin = (time_gap.total_seconds() )/ 30
        estimate_time = df_filtered.iloc[idx]['EstimateTime']
        e = abs(estimate_time - time_gap_halfmin)/2
        time_list.append(e)
        
    return time_list, len(df_filtered)
    
if __name__ == "__main__":
    
    
    df = detect("Xinglong Shanzhuang", 0)    
    print(df)
  

    
def cal(data):
    mean_val = np.mean(data)
    std_sample = np.std(data, ddof=1)
    
    return mean_val,std_sample

