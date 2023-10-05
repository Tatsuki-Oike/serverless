import requests
import config

# 0 設定
API_URL = config.API_URL
DATA = {'image_name': 'cat.jpg'}
LOCAL_IMAGE = '../cat.jpg'

def response_function(response):
    print('url: ', response.url)
    print('status code: ', response.status_code)
    print('response: ', response.json())
    print("--------------------------------------")


# 1 POSTリクエスト
print("POST")
response = requests.post(API_URL, json=DATA)
response_function(response)


# 2 Presigned urlで画像アップロード
print("PRESIGNED")
presigned_url = response.json()["presigned_url"]
with open(LOCAL_IMAGE, 'rb') as file:
    response = requests.put(presigned_url, data=file)
print('status code: ', response.status_code)
print("--------------------------------------")

# 3 GETリクエストを送信
print("GET")
response = requests.get(API_URL)
response_function(response)