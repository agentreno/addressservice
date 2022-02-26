# addressservice

## Setup

This project uses poetry for dependency management and virtual environment,
start with `pip install poetry` if necessary and then `poetry install` and
`poetry shell`.

To setup the local sqlite database run `python addressservice/manage.py
migrate`.

This uses
[django-cities-light](https://github.com/yourlabs/django-cities-light) to
source some standardised country, city and region data.

Run `python manage.py cities_light --progress --force-import-all` to populate
the database with that data.

Depending on your connection, that could take 5-10 minutes, so the API is
usable without it since the foreign key fields are nullable, but it requires
leaving city null, or pre-populating it via the admin console.

Finally run `python manage.py runserver` and navigate to
`http://localhost:8000/`.
