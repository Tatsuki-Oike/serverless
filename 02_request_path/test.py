import os
import json
import requests

# 0 設定

API_URL = 'https://XXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/test'
DATA = {
    'key1': 'value1',
    'key2': 'value2'
}

def response_function(response):
    print('url: ', response.url)
    print('status code: ', response.status_code)
    print('response: ', response.json())
    print("--------------------------------------")


# 1 HTTPリクエスト

## 1.1 GETリクエストを送信
print("--------------------------------------")
print("GET")
response = requests.get(API_URL, params=DATA)
response_function(response)
    
## 1.2 POSTリクエストを送信
print("POST")
response = requests.post(API_URL, data=json.dumps(DATA))
response_function(response)

## 1.3 PUTリクエストを送信
print("PUT")
response = requests.put(API_URL, json=DATA)
response_function(response)

## 1.4 PATCHリクエストを送信
print("PATCH")
response = requests.patch(API_URL, json=DATA)
response_function(response)

## 1.5 DELETEリクエストを送信
print("DELETE")
response = requests.delete(API_URL, params=DATA)
response_function(response)


# 2 パスの変更
USER_URL = os.path.join(API_URL, "user")
ID_URL = os.path.join(USER_URL, "1")

## 2.1 USER GETリクエストを送信
print("--------------------------------------")
print("USER GET")
response = requests.get(USER_URL, params=DATA)
response_function(response)

## 2.2 ID GETリクエストを送信
print("--------------------------------------")
print("ID GET")
response = requests.get(ID_URL, params=DATA)
response_function(response)
