# running results
Open source system to manage running result for sports clubs
* Python https://www.python.org/
* Django framework https://www.djangoproject.com/
* Docker https://www.docker.com/

Please use the develop branch as the target for pull requests for ongoing development.

## Status
Development phase

## Features
* Import of data
* Export of data
* Administration of user for the gathering of the data
* Public access to
* record list
* Annual record list
* Annual result lists of every distance and for age groups
* List of events

## Requirements
* Docker

## Tutorial
https://github.com/ad-software/running_results/wiki/Tutorial

# Quick Start
`$ git clone https://github.com/ad-software/running_results`

`$ cd running_results`

Edit .env files
* .env
* running_results/.env

**.env**

`POSTGRES_PASSWORD=<PASSWORD>`

**running_results/.env**

```
ALLOWED_HOSTS=<localhost,127.0.0.1 for Test, or public ip>
DB_NAME=<name of database>
DB_USER=<name of user for database>
DB_PASSWORD=<PASSWORD>
DEBUG=<True or False>
SECRET_KEY=<Django secret>
```

If DEBUG equals "True", ALLOWED_HOSTS can be empty.

For local testing use: localhost,127.0.0.1

    docker compose up

## Database

### Database Tables
Now run migrations to create database tables for the apps.
'docker compose exec web python manage.py makemigrations'
'docker compose exec web python manage.py migrate'

## Admin User
Create an admin superuser:
'python manage.py createsuperuser'

# Open web site
http://localhost:8000

## Language Settings

## Getting Help

## Contributors

## Demo

# Development
## Virtualenv
Installation of virtualenv
    pip install virtualenv

On Debian/Ubuntu systems
    apt install python3.10-venv

Creation of virtual env
    python3 -m venv venv

Activation of virtual env
    source venv/bin/activate

Installation of requirements
    pip install -r requirements.txt

## PyLint
https://learndjango.com/tutorials/pre-commit-django

## Cleanup

# Adminer
Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP

https://hub.docker.com/_/adminer/

http://localhost:8080

System: PostgreSQL
Server: db:5432 (the service name from docker-compose.yml)
Username: .env
Password: .env
Database: .env


python manage.py migrate
python manage.py runserver
