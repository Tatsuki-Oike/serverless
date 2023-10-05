# 0 AWS

* Lambda関数の作成
* API Gatewayの作成 (REST API)
  * GET, POST, PUT, PATCH, DELETE作成
  * リソースを追加(user)
  * URLパラメータを追加(id)

# 1 Lambda関数の内容

```python
import json

def lambda_handler(event, context):
    try:
        response = {
            "status": "SUCCESS",
            "query": event.get('queryStringParameters'), # GET, DELETE
            "data": event.get('body'), # POST, PUT, PATCH
            "params": event.get('pathParameters'), # パスパラメータ
        }
        status_code = 200
    except Exception as e:
        response = {
            "status": "ERROR",
            "details": str(e)
        }
        status_code = 500
    return {
        'statusCode': status_code,
        'body': json.dumps(response)
    }
```

<br>
```python
response = {
    "status": "SUCCESS",
    "event": event,
    "query": event.get('queryStringParameters'), # GET, DELETE
    "data": event.get('body'), # POST, PUT, PATCH
    "params": event.get('pathParameters'), # パスパラメータ
    }
```

# 2 Pythonでテスト

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

```sh
cd ./02_request_path
python3 test.py
```