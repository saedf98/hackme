
# Clear
cd ../apps;

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# optional based on db type(sqlite)
# rm ../db.sqlite3

# Migrate
cd ../;
# optional based on db type
python manage.py reset_db

python manage.py makemigrations
python manage.py migrate

python manage.py makesuperuser
