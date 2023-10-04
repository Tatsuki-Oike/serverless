import base64
import requests

# 設定
DEBUG_FLG = True

if DEBUG_FLG:
    API_URL = "http://localhost:9000/2015-03-31/functions/function/invocations"
else:
    API_URL = "https://XXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/test"

RESIZE_IMAGE = "../images/output.jpg"

POST_DATA = {
    'image_b64': '',
}    

# 画像をbase64形式に
print("\nLoad Image")
with open(RESIZE_IMAGE, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")
POST_DATA["image_b64"] = image_b64

# POSTリクエスト送信
print("POST")
response = requests.post(API_URL, json=POST_DATA)
print('status code: ', response.status_code)
print('response: ', response.json())