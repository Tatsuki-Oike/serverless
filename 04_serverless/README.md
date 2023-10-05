# 0 AWS

* S3の作成
  * パブリックアクセスをすべてブロック オフ
  * バケットポリシー変更
  * Cross-Origin Resource Sharing (CORS)
* DynamoDBの作成
  * image_id, image_name, image_url
* Lambda関数の作成
  * 3つのlambda関数の作成
  * S3, DynamoDBのフルアクセス許可
* API Gatewayの作成 (REST API)
  * GET, POST, DELETE作成
  * CORS有効化

<br>
バケットポリシー変更

```js
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucket-name/*"
        }
    ]
}
```

<br>
Cross-Origin Resource Sharing (CORS)

```js
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]
```

<br>

# 1 Lambda関数の内容

## 1.1 GETリクエスト

```python
import json
import boto3

bucket_name = "bucket-name"
table_name = "table-name"

db = boto3.resource("dynamodb")
table = db.Table(table_name)

headers = {
        'Content-Type': 'application/json',  # レスポンスのコンテンツタイプを指定
        'Access-Control-Allow-Origin': '*',  # CORSの設定 (すべてのオリジンを許可)
        'Access-Control-Allow-Methods': 'GET',  # 許可するHTTPメソッドを指定
        'Access-Control-Allow-Headers': 'Content-Type',  # 許可するカスタムヘッダーを指定
        'Access-Control-Allow-Credentials': 'true'  # クッキーや認証情報を許可
    }

def lambda_handler(event, context):
    try:
        # テーブルの中身取得
        table_items = table.scan()
        items = table_items.get("Items")
        while table_items.get("LastEvaluateKey"):
            table_items = table.scan(ExclusiveStartKey=r["LastEvaluatedKey"])
            items.extend(table_items["Items"])
            
        response = {
            "status": "SUCCESS",
            "items": items,
        }
        status_code = 200
    except Exception as e:
        response = {
            "ERROR": str(e)
        }
        status_code = 500
    return {
        'statusCode': status_code,
        "headers": headers,
        'body': json.dumps(response)
    }
```

## 1.2 POSTリクエスト

```python
import json
import uuid
import boto3
from botocore.config import Config

bucket_name = "bucket-name"
table_name = "table-name"

s3 = boto3.client(
    's3',  
    region_name='ap-northeast-1',
    endpoint_url='https://s3-ap-northeast-1.amazonaws.com',
    config=Config(signature_version="s3v4"),
    )
    
db = boto3.resource("dynamodb")
table = db.Table(table_name)

headers = {
        'Content-Type': 'application/json',  # レスポンスのコンテンツタイプを指定
        'Access-Control-Allow-Origin': '*',  # CORSの設定 (すべてのオリジンを許可)
        'Access-Control-Allow-Methods': 'POST',  # 許可するHTTPメソッドを指定
        'Access-Control-Allow-Headers': 'Content-Type',  # 許可するカスタムヘッダーを指定
        'Access-Control-Allow-Credentials': 'true'  # クッキーや認証情報を許可
    }

def lambda_handler(event, context):
    try:
        # データ受け取り
        json_data = json.loads(event["body"])
        image_name = json_data["image_name"]

        # Presigned URL取得
        presigned_url = s3.generate_presigned_url(
                "put_object",
                Params={'Bucket': bucket_name, 'Key': image_name},
                ExpiresIn=600  # 有効期限（秒単位）を設定
            )

        # テーブルに項目追加
        image_url = f'https://{bucket_name}.s3.amazonaws.com/{image_name}'
        image_id = str(uuid.uuid4())
        db_resp = table.put_item(
            Item={
                "image_id": image_id,
                "image_name": image_name,
                "image_url": image_url
                }
            )

        response = {
            "status": "SUCCESS",
            "image_id": image_id,
            "presigned_url": presigned_url,
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
        "headers": headers,
        'body': json.dumps(response)
    }
```

## 1.3 DELETEリクエスト

```python
import json
import boto3

from botocore.config import Config

s3 = boto3.client(
    's3',  
    region_name='ap-northeast-1',
    endpoint_url='https://s3-ap-northeast-1.amazonaws.com',
    config=Config(signature_version="s3v4"),
    )

bucket_name = "bucket-name"
table_name = "table-name"

db = boto3.resource("dynamodb")
table = db.Table(table_name)

headers = {
        'Content-Type': 'application/json',  # レスポンスのコンテンツタイプを指定
        'Access-Control-Allow-Origin': '*',  # CORSの設定 (すべてのオリジンを許可)
        'Access-Control-Allow-Methods': 'DELETE',  # 許可するHTTPメソッドを指定
        'Access-Control-Allow-Headers': 'Content-Type',  # 許可するカスタムヘッダーを指定
        'Access-Control-Allow-Credentials': 'true'  # クッキーや認証情報を許可
    }

def lambda_handler(event, context):
    try:
        # データ受け取り
        query_data = event['queryStringParameters']
        image_id = query_data["image_id"]

        # S3のデータ消去
        db_resp = table.get_item(
            Key={"image_id": image_id}
        )
        object_key = db_resp["Item"]["image_name"]
        s3.delete_object(Bucket=bucket_name, Key=object_key)

        # テーブルの項目消去
        table.delete_item(
            Key={"image_id": image_id},
        )

        response = {
            "status": "SUCCESS",
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
        'headers': headers,
        'body': json.dumps(response)
    }
```

<br>

# 2 Pythonでテスト

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

```sh
cd ./04_serverless/code
python3 test.py
python3 delete.py
```