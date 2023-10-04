# 1 Docker環境でzipファイルの作成

```sh
cd ./06_lambda_zip
docker build -t lambda-zip .
docker run --rm -it --name zip_container -v "$PWD:/src" lambda-zip /bin/sh -c "cp -r python /src; cp library.zip /src; exit"
docker image rm lambda-zip
```

<br>

# 2 Lambda関数で外部ライブラリ利用

* Lambda関数作成
  * zipファイルアップロード
  * import pandas as pd