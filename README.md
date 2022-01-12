# RNG

A web application allowing users to rate and discuss relatively new games.


## Team Members

Jason Cook(2328261c) Alasdair Russel(2315645r) Ross Johnstone(2326663j) Jamie Allan(2316615a) Liam Brodie(2315645r)

## PythonAnywhere

http://ratenewgameswad2.pythonanywhere.com/rng/


## Running Instructions

git clone https://github.com/JAA1999/WAD_Project.git

pip install -r requirements.txt

cd Wad_Project

python manage.py makemigrations

python manage.py migrate

python manage.py migrate --run-syncdb

python populate_rng.py 

python manage.py runserver

python manage.py createsuperuser