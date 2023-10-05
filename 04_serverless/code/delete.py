import requests
import config

# 0 設定
API_URL = config.API_URL
DELETE_DATA = {'image_id': 'XXXXXXXXXXXXXXXXXXXXXX'}

def response_function(response):
    print('url: ', response.url)
    print('status code: ', response.status_code)
    print('response: ', response.json())
    print("--------------------------------------")

# 4 DELETEリクエストを送信
print("DELETE")
response = requests.delete(API_URL, params=DELETE_DATA)
response_function(response)