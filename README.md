# running results
Open source system to manage running result for sports clubs
* Python
* Django framework
* Docker

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
+ Docker Compose

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

`docker-compose up`




## Database

### Database Tables
Now run migrations to create database tables for the apps.
'docker-compose exec web python manage.py makemigrations'
'docker-compose exec web python manage.py migrate'

## Admin User
Create an admin superuser:
'python manage.py createsuperuser'

## Language Settings

## Getting Help

## Contributors

## Demo

