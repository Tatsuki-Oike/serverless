# 0 AWS

* Lambda関数の作成
* API Gatewayの作成 (REST API)
  * GETメソッド追加
  * Lambda関数連携

# 1 Lambda関数の内容

```python
import json

def lambda_handler(event, context):
    try:
        response = {
            "status": "SUCCESS",
            "event": event,
        }
        status_code = 200
    except Exception as e:
        response = {
            "ERROR": str(e)
        }
        status_code = 500
    return {
        'statusCode': status_code,
        'body': json.dumps(response)
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
cd ./01_lambda
python3 test.py
```