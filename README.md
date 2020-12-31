# running results
Open source system to manage running result for sports clubs based on Django framework.

Please use the develop branch as the target for pull requests for on-going development.

## Status
first code and conception phase

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
requirements.txt

and ...

## Documentation
CCS with Bootstrap

## Tuturial
https://github.com/ad-software/running_results/wiki/Tutorial

## Quick Start
```
$ pip install --upgrade virtualenv
$ python3 -m venv env
$ source env/bin/activate

(env) $ pip3 install -r  requirements.txt
(env) $ python manage.py
```

## Environment setup
Create the file running_results/.env with the following parameter

```
ALLOWED_HOSTS=
DEBUG=
SECRET_KEY=`
```


## Database

### Database Tables
Now run migrations to create database tables for the apps.
python manage.py migrate

## Admin User
Create an admin superuser:

python manage.py createsuperuser

## Language Settings

## Getting Help

## Contributors

## Demo

