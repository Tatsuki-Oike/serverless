# 1 学習済みモデルの準備

## 1.1 学習済みモデルのダウンロード

```sh
cd ./07_lambda_docker/model
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r ../app/requirements.txt
```

```sh
python3 model.py
```

## 1.2 S3に学習済みモデルのアップロード

* モデル保存用のS3の作成
  * アクセス許可設定
  * モデルをアップロード

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

# 2 ローカルでテスト

```sh
cd ../app
docker build -t detection-image:test .
docker run --rm --name lambda_container -p 9000:8080 detection-image:test
```

<br>
ターミナルをもう一つ作成

```sh
cd ./07_lambda_docker/test/code
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install requests
python3 -m pip install pillow
```

<br>
DEBUG_FLG = True

```sh
python3 resize.py
python3 test.py
```

```sh
docker image rm detection-image:test
```

<br>

# 3 AWSサービスを利用してデプロイ

## 3.1 サービス作成

* ECRでリポジトリ作成
* cloud9の環境利用
  * EC2のストレージ変更(100GB)

## 3.2 ストレージの容量変更

```sh
df -h
lsblk
sudo resize2fs /dev/<lsblkで表示されるファイル>
sudo reboot
df -h
```

## 3.3 Gitでソースコードclone

```sh
git --version
git clone https://github.com/Tatsuki-Oike/serverless.git
cd ./serverless/07_lambda_docker/app
```

# 4 ECRにイメージをデプロイ

* ECRのリボジトリのプッシュ方法をコピペ

<br>

# 5 Lambdaにデプロイ

## 5.1 AWSサービス

* Lambdaを作成
  * 設定でメモリと時間変更
* API gatewayを作成

## 5.2 テスト

* Lambdaでテスト
* ローカルからテスト

<br>
cloud9からローカルに移動
DEBUG_FLG = False

```sh
python3 test.py
```