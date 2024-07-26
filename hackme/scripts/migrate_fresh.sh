
# Clear
cd ../apps;

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# optional based on db type
rm ../db.sqlite3

# Migrate
cd ../;
python manage.py makemigrations
python manage.py migrate