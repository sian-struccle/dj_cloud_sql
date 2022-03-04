# ローカルでの起動方法

## 前提条件
```
docker環境がある
```

## clone & cd
```
git clone https://github.com/sian-struccle/dj_cloud_sql.git
cd dj_cloud_sql
```

## .envファイルを作成し、下記環境変数を入力(本番環境でのご利用はご注意ください。)
```
DEBUG=1
SECRET_KEY=struccle
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 127.0.0.1:5432 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=struccle_db
SQL_USER=struccle
SQL_PASSWORD=struccle
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

## Djangoアプリ起動（docker）
```
docker-compose up -d --build
```

## migrateをする
```
docker-compose exec web python manage.py migrate --noinput
```

## localhostへアクセス
```
# 8000は不要
http://localhost/
```

## cloud SQLの適用
こちらの動画をご参照ください。
https://youtu.be/KUp35Tq0-94
