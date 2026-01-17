# 1. ベースイメージ：最新の Python 3.11 を使用（動作の安定性と最新機能のため）
FROM python:3.11

# 2. コンテナ内の作業ディレクトリを /app に固定
WORKDIR /app

# 3. ライブラリのインストール：Flask（Webフレームワーク）やSQLAlchemy（DB操作）、psycopg2（PostgreSQL接続）を一括導入
RUN pip install flask flask-sqlalchemy psycopg2-binary

# 4. ソースコードのコピー：ホスト（PC）側のカレントディレクトリ内の全ファイルをコンテナの /app へ転送
COPY . .

# 5. 実行コマンド：コンテナ起動時にメインプログラム（main.py）を直接実行
CMD ["python", "main.py"]