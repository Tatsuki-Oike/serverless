# 0 AWS

* DynamoDBの作成
* Lambda関数の作成
  * DynamoDBフルアクセスの権限追加

# 1 Lambda関数の内容

<br>
DynamoDBにitem追加

```python
import json
import boto3

db = boto3.resource("dynamodb")
table = db.Table("sampleTable")

def lambda_handler(event, context):
    try:
        
        db_resp = table.put_item(
            Item={
                "user_id": "0",
                "username": "Tatsuki"
                }
            )
            
        response = {
            "status": "SUCCESS",
            "db_resp": db_resp,
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
DynamoDBのitem取得

```python
db_resp = table.get_item(
            Key={"user_id": "0"}
        )
```

<br>
DynamoDBのitem更新

```python
db_resp = table.update_item(
            Key={"user_id": "0"},
            UpdateExpression="SET username = :value",
            ExpressionAttributeValues={
                ":value": "Akira",
            }
        )
```

<br>
DynamoDBのitem消去

```python
db_resp = table.delete_item(
            Key={"user_id": "0"},
        )
```

<br>

# 2 Query and Scan

## 2.1 データの作成とQuery

<br>
複数のデータを追加

```python
data = []

for i in range(1, 21):
    item = {
        "user_id": str(i),
        "username": f"Name {i}"
    }
    data.append(item)

with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)
    
db_resp = None
```

<br>
Query

```python
from boto3.dynamodb.conditions import Key

db_resp = table.query(
            KeyConditionExpression=Key("user_id").eq("3")
        )
```

## 2.2 Scan

<br>
Scan

```python
table_items = table.scan()
db_resp = {
    "number": len(table_items.get("Items")),
    "items": table_items
}
```

<br>
Scan (データ量が多い場合)

```python
table_items = table.scan()
items = table_items.get("Items")
while table_items.get("LastEvaluateKey"):
    table_items = table.scan(ExclusiveStartKey=r["LastEvaluatedKey"])
    items.extend(table_items["Items"])
db_resp = {
    "number": len(items),
    "items": items
}
```

<br>
Scan (条件一致)

```python
from boto3.dynamodb.conditions import Attr

table_items = table.scan(
    FilterExpression=Attr("username").eq("Name 4"),
    ProjectionExpression="username"
)
db_resp = {
    "number": len(table_items.get("Items")),
    "items": table_items
}
```

<br>
複数のデータを消去

```python
data = []

for i in range(1, 10):
    item = {
        "user_id": str(i),
    }
    data.append(item)

with table.batch_writer() as batch:
    for item in data:
        batch.delete_item(Key=item)
        
db_resp = None
```