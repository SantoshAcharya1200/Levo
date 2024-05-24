# Calendar Scheduling Application

## Table of contents

1. [Description](#description)
2. [Screenshots](#screenshots)
3. [Installation and Usage](#installation-usage)

## Description <a name="description"></a>

This is a calendar scheduling application using Django for the backend and React for the frontend. The application allows users to manage their calendars, view holidays, create events, and receive notifications for scheduled events.

<ins>Features:</ins>

- View the calendar with holidays and events
- Create,edit and delete event
- Receive notifications of events at the scheduled time





## Screenshots <a name="screenshots"></a>
![calendar](https://github.com/SantoshAcharya1200/Levo/assets/41406942/f6a9b5ef-c440-4403-a238-18c3f27ef8f8)

![event-list](https://github.com/SantoshAcharya1200/Levo/assets/41406942/ee3c8618-5412-4ad9-b301-5f2df272307c)

![create-new-event](https://github.com/SantoshAcharya1200/Levo/assets/41406942/40b68dcd-9d70-41f7-93c1-eac62d84b015)


## API Documentation <a name="api-documentation"></a>

All the endpoints are listed below.

- <ins>Events</ins>:

  - `/api/events/` - POST, GET

All the routes are listed below.
- `http://localhost:3000/` - Calender with all holidays and events
- `http://localhost:3000/events/` -Lists of all the events
- `http://localhost:3000/events/id` -Update, Delete event
- `http://localhost:3000/holidays/` -Lists holidays



## Installation and Usage <a name="installation-usage"></a>

#### <ins>**General**</ins>

- Requirements:
  - `node >= 16.14.0`
  - `npm >= 8.3.1`
  - `python >= 3.8`
  - `pip >= 21.3.1` 
- `git clone https://github.com/SantoshAcharya1200/Levo.git` - clones the repository
- `cd LEVO`

#### <ins>**For frontend folder**</ins>

- Setup the project as per _General_ sub-section
- `cd frontend`
- `npm install` or `npm i` - installs all packages
- `npm install --save-dev` - installs devDependencies
- `npm start` - starts the app

#### <ins>**For backend folder**</ins>

- Setup the project as per _General_ sub-section
- `cd backend`
- `py -m venv yourVenvName` - creates a virtual environment
- `yourVenvName\Scripts\activate.bat` - activates the virtual environment
- `cd calendar_project`
- `pip install -r requirements.txt` - installs all modules
- `python manage.py makemigrations` & `python manage.py migrate` - migrates all the tables to db
- `python manage.py createsuperuser` - creates a superuser
- `python manage.py runserver` - runs the server

> NOTE: First run backend server (it will run on `http://127.0.0.1:8000`), then run frontend app (it will run on `http://localhost:3000/`)

#### <ins>**For Celery with redis**</ins>
- Start Redis server(make sure you have redis intalled):
- `redis-server`
- Start Celery worker:
- `celery -A calendar_project worker --loglevel=info`
