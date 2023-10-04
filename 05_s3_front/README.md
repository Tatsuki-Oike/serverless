# 1 ローカルでフロントエンド開発

https://nodejs.org/en/download

```sh
npm install -g @vue/cli
```

```sh
cd ./05_s3_front
npm init vite-app frontend
cd frontend
npm install
npm install axios
npm install vue-router
npm install vuex
npm run dev
npm run build
```

# 2 S3にアップロード

## 2.1 S3の設定

* バッケットを作成
* バケット設定
  * 「パブリックアクセスをすべて ブロック」のチェックを外す
  * 「静的ウェブサイトホスティング」有効化
  * バケットポリシー編集

```sh
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::[bucket-name]/*"
            ]
        }
    ]
}
```

## 2.2 WEBアプリのアップロード

* オブジェクト > アップロード
* distフォルダの中身をアップロード
* プロパティ > 静的ウェブサイトホスティングのURLにアクセス

<br>