# 1 Docker環境でzipファイルの作成

```sh
cd ./06_lambda_zip
docker build -t lambda-zip .
docker run --rm -it --name zip_container -v "$PWD:/src" lambda-zip /bin/sh -c "cp -r python /src; cp library.zip /src; exit"
docker image rm lambda-zip
```

<br>

# 2 Lambda関数で外部ライブラリ利用

## 2.1 zipファイルなしでLambda関数テスト

* Lambda関数作成
* テスト

```python
import json
import requests

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(str(requests.__version__))
    }

```

<br>

# 2.2 zipファイルを追加してLambda関数テスト

* zipファイルをアップロードしてLambda関数と連携
* 再度テスト
