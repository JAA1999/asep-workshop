# RNG

A web application allowing users to rate and discuss relatively new games.

## Running Instructions

git clone https://github.com/JAA1999/WAD_Project.git

pip install -r requirements.txt

cd WAD_Project

python manage.py makemigrations

python manage.py migrate

python manage.py migrate --run-syncdb

python populate_rng.py 

python manage.py runserver

python manage.py createsuperuser