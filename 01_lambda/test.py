import requests

API_URL = 'https://XXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/test'
PARAMS = {
    'key1': 'value1',
    'key2': 'value2'
}

# GETリクエストを送信
response = requests.get(API_URL, params=PARAMS)
print('status code: ', response.status_code)
print('response: ', response.json())
print("--------------------------------------")