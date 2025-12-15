import config
import fetcher_module
import process
def main():
   
    url = config.url
    app_id = config.bus_api_key.get("client_id")
    app_key = config.bus_api_key.get("client_secret")
    auth_url = config.auth_url
    
    
    print("正在取得 Token...")
    auth_obj = fetcher_module.Auth(app_id, app_key)
    
    try:
     
        auth_response = fetcher_module.requests.post(
            auth_url, 
            data=auth_obj.get_auth_payload(),
            headers=auth_obj.get_auth_headers()
        )
        auth_response.raise_for_status()
    except Exception as e:
        print(f"取得 Token 失敗: {e}")
        return None

    
    print("正在取得公車資料...")
    try:
        data_obj = fetcher_module.Data(app_id, app_key, auth_response)
        data_response = fetcher_module.requests.get(
            url, 
            headers=data_obj.get_data_header()
        )
        data_response.raise_for_status()
        return data_response
    except Exception as e:
        print(f"取得資料失敗: {e}")
        return None

if __name__ == "__main__":
    dataresponse = main()
    
    if dataresponse:
        
        write_in_data = process.get_time(dataresponse.json())
        process.write_to_file(write_in_data)
        print("資料處理完成，已寫入 parquet。")
    else:
        print("程式終止，未取得資料。")