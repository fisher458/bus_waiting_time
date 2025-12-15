import probability

if __name__ == "__main__":
    station_name = input("哪一站")
    estimate_time = int(input("顯示等多久"))
    direction = int(input("往動物園輸入1,台北車站輸0"))
    
    time_error, lenth = probability.detect(station_name,direction,estimate_time)
    mean, std = probability.cal(time_error)
    print(f"預估等待時間為{estimate_time+mean}分鐘")