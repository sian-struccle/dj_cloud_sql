# オフィシャルイメージをpull
FROM python:3.8.0-alpine

# ワーキングディレクトリ（/usr/src/app以降のコードを実行する場所）を設定
WORKDIR /usr/src/app

# .pycの不要なファイルを生成しないよう設定
ENV PYTHONDONTWRITEBYTECODE 1
# 標準出力・標準エラーのストリームのバッファリングを行わないよう設定
ENV PYTHONUNBUFFERED 1

# python&postgreSQLに必要なソフトウェアをインストール
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# pipをアップグレードし、ライブラリをインストール
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# entrypoint.shをコピーし、書き込み権限を付与
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# プロジェクトをコピーする
COPY . .

# entrypoint.shを実行する => bash entrypoint.shと同義
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
