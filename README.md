# addressservice

## TODO

User will not be able to add a duplicated address to their account
- Put a UniqueConstraint on the model

User is able to retrieve a large number of address entries in a practical way
- Turn on pagination

User is able to filter retrieved addresses using request parameters
- Turn on SearchFilter

User is able to delete multiple addresses
- Not doing

User is able to authenticate with a username and a password
User can log out
- Look into Istio RequestAuthentication and using it to signal context to the
  API service

## Setup

This uses
[django-cities-light](https://github.com/yourlabs/django-cities-light) to
source some standardised country, city and region data.

In addition to the standard makemigrations and migrate, run `python manage.py
cities_light --progress --force-import-all` to populate the database with that
data.

Depending on your connection, that could take 5-10 minutes, so the API is
usable without it since the foreign key fields are nullable, but it requires
leaving city null, or pre-populating it via the admin console.
