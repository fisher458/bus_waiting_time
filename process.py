import config
import fetcher_module
from pprint import pprint
import pandas as pd
import os
file = config.file
columns = config.column
def get_time(data,counter=0):
    write_in_buffer = []
    
    for item in data:
        
        raw_time = item.get('EstimateTime')
        
        
        if raw_time is not None:
            
            calculated_time = raw_time / 30 
            
            
        else:
            
            calculated_time = -1 

        tup_buffer = (
            counter,
            item['Direction'],
            item['StopName']['En'],
            item['SrcUpdateTime'],
            calculated_time  
        )
        write_in_buffer.append(tup_buffer)
        
    return write_in_buffer      

def create_csv_header(path, columns):
    if not os.path.exists(path):
        # 創建一個空的 DataFrame，並設定 column 名稱
        empty_df = pd.DataFrame(columns=columns)
        
        # 寫入檔案，mode='w' (寫入/覆蓋)，header=True
        empty_df.to_csv(path, index=False, mode='w', header=True, encoding='utf-8')
        print(f"✅ 成功創建檔案 '{path}' 並寫入 column 標題。")
    else:
        print(f"檔案 '{path}' 已存在，跳過標題創建。")
        

def write_to_file(data):
    new_df = pd.DataFrame(data, columns=columns)
    new_df.to_csv(file, index=False, mode='a', header=False, encoding='utf-8')
    print(f"✅ 成功追加 {len(new_df)} 筆數據到檔案 '{file}'。")
    
    return 1

