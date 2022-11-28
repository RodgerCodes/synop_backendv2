# SYNOP BACKEND

This is the rest api for the synop mobile app, which is an app that meteorologist can use to encode weather data into the main synoptic code (FM-12) and send all the data to the main meteorological office.

## Requirements

1. [Python 3](https://www.python.org/)
2. [Postgresql](https://www.postgresql.org/download/)

# Project setup

```
git clone https://github.com/RodgerCodes/synop_backendv2
```

```
virtualenv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```
python manage.py runserver
```
