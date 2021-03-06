# RNG

This is a web application allowing users to rate and discuss relatively new games.

## Running Instructions

Create a directory that you're happy to use for the purposes of this workshop

### Setup your environment and clone the repo
```
git clone https://github.com/JAA1999/asep-workshop.git
cd asep-workshop
python -m venv .venv
```

Navigate to .venv\Scripts\ and run the appropriate activate script depending on your OS

To deactivate it just enter deactivate into the prompt

```
pip install -r requirements.txt
```

### Setup the app and run it
Navigate to asep-workshop and run these commands (use python3 on a linux-like OS)
```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python populate_rng.py
python manage.py createsuperuser  # this is so you can login to the app
                                  # the details you provide are not important
                                  # but you will need to use them
                                  # I recommend "admin123" as your password
                                  # Django is a bit picky
python manage.py runserver
```