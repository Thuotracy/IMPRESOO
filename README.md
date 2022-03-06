# PITCH
##Developer
Tracy Wangari

## Description
In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful?
This application allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

#### Link to deployed site
http://pitch.herokuapp.com/

## Table of content
1. [Description](#description)
2. [API endpoints](#endpoints)
3. [Setup and installations](#setup-and-installations)
4. [Deployment](#deployment)
5. [Contributing](#contributing)
6. [Bugs](#bugs)
7. [Contact me](#support-and-contact-details)
8. [Licensing](#license)


## Setup and installations

#### Prerequisites
1. [Python3.8](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
5. 

#### Technologies used
    - Python 3.8
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    -SQLAlchemy



#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
NAME='tutorial'
USER='<Username>'
PASSWORD='<password>'
HOST='localhost'
MODE='dev'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE tutorial;
```

#### Make and run migrations
```bash
python3.8 manage.py makemigrations && python3.8 manage.py migrate
```

#### Run the app
```bash
./start.sh
```
Open [localhost:8000](http://127.0.0.1:5000/)


## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
#### Known bugs
 - none yet


## Support and contact details
Incase of any inquires reach me out at tracyjacobs775@gmail.com

### License
MIT

Copyright (c)2022 **Tracy Wangari**