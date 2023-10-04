# 0 AWSのサービス

## 0.1 サービス作成

* モデル保存用のS3の作成
  * アクセス許可設定
* ECRでリポジトリ作成
* cloud9の環境利用
  * EC2のストレージ変更(100GB)

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

## 0.2 ストレージの容量変更

```sh
df -h
lsblk
sudo resize2fs /dev/<lsblkで表示されるファイル>
sudo reboot
df -h
```

## 0.3 Gitでソースコードclone

```sh
sudo yum install -y git
git --version
git clone https://github.com/Tatsuki-Oike/aws_service.git
cd ./serverless
```

# 1 学習済みモデルの準備

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

```sh
python3 test.py
```

```sh
docker image rm docker-image:test
docker image prune -a
docker container prune -f
```

<br>

# 3 ECRにイメージをデプロイ

* ECRのリボジトリのプッシュ方法をコピペ

<br>

# 4 Lambdaにデプロイ

* Lambdaを作成
  * 設定でメモリと時間変更
* API gatewayを作成