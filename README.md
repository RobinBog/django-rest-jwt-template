# Django Restfull JWT Template
## Description
This is a template for a django project.

## Main Features
- Authentication with JWT
- Register/Login with EMail instead of username

## Routes
* /user
    * /register/
    * /logout/blacklist/
    * /api-token/
    * /api-token-refresh/
* /posts

# Installation 🚀
## prerequisite
1. Check if Python is installed on your machine with a version > 3.0 ``` python --version ```

## with a virtual evironment
1. Create a virtual environemt ```python3 -m venv venv```
2. choose the venv ```source venv/bin/activate```
2. Install all requirements for the App ```pip install -r requirements.txt```
3. Start the Server ```python manage.py runserver```

## with Docker-Compose -> Not setup yet
To run the Docker Container make sure you installed docker on your machine ``` docker -v ```

1. start Docker on your machine
2. Run the Command ```docker-compose up --build``` to start a container running the app
3. The App will be avaiable at localhost:8000

# Testing ✅
Install ```coverage``` in your virtual environment to peform the tests.
```pip install coverage```

Run the test in your virtual environment.
```coverage run --omit='*/venv/*' manage.py test```

Create a Coverage Report of the WebApp. Open the index.html file in the newly created directory to see the test coverage of the app.
```coverage html```
