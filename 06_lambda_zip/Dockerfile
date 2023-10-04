FROM public.ecr.aws/sam/build-python3.11

# 必要なライブラリをインストール
COPY requirements.txt /var/task/requirements.txt

# 作業ディレクトリを/var/taskに設定
WORKDIR /var/task

# zipファイル作成
RUN python3 -m pip install --upgrade pip && \
    pip install -r /var/task/requirements.txt -t python/lib/python3.11/site-packages/ && \
    zip -r library.zip python