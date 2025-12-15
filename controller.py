import peridoc_fetch
import time
from datetime import datetime
import process
excution_counter = 0
print("程式開始執行...")





print("--- 主控台啟動 ---")

try:
    while True:
        now = datetime.now()
        
        if 7 <= now.hour < 22:
            
            try:
                data = peridoc_fetch.main()
                write_in_data = process.get_time(data.json(),excution_counter)
                process.write_to_file(write_in_data)
                print(f"資料處理完成，已寫入 parquet。執行次數: {excution_counter}")
                excution_counter += 1
                
            except Exception as e:
                print(f"執行錯誤: {e}")
            
            
            time.sleep(30) 
            
        else:
            time.sleep(60)

except KeyboardInterrupt:
    print("\n系統安全關閉")
