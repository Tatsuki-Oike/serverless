# 使用するLambdaランタイムのベースイメージ
FROM public.ecr.aws/lambda/python:3.11

# ファイルをコピー
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# 必要なパッケージをインストール
RUN pip install -r requirements.txt

# Lambda関数のハンドラを指定
CMD [ "lambda_function.handler" ]
