FROM python:3.11
WORKDIR /app

# ライブラリのインストール
RUN pip install flask flask-sqlalchemy psycopg2-binary

# 今いる場所（student-appフォルダ）の「中身」をDockerにコピー
COPY . .

# 実行コマンド（パスをシンプルにします）
CMD ["python", "main.py"]