# movie-app-ak

This is a simple API to access a Database of movies and actors.

## Motivation
I made this app to develop my skills as a fullstack web developer and as the capstone project for the FSND course at Udacity.

## GETTING STARTED
 Base URL: https://movie-app-ak.herokuapp.com This App currently does not have a Frontend so there is nothing present at the base URL

 Authentication: Uses token Authentication. 

 Also has three roles which have access to specific endpoints:
    Casting Assistant
        Can view actors and movies

    Casting Director
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies

    Executive Producer
        All permissions a Casting Director has and…
        Add or delete a movie from the database

Temporary tokens for each role are included at the end of the README.


## Installing Dependencies
# Python 3.9
Follow instructions to install the latest version of python in the python docs
https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python

# Virtual Environment
Setup your virtual environment and install dependencies by running:
pip install -r requirements.txt
in the project directory

# Key Dependencies
Flask: a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy: the Python SQL toolkit and ORM we'll use  to handle the postgres database.


## Environmental Variables
setup.sh file includes env variables needed to run the app
these can be changed to fit the database url and authorization variables.
they will then need to be expoted again to run the app
run:
source setup.sh


## Runnning the Server
From within the project folder and with the Virtual environment running run these commands:

export FLASK_APP=app.py
flask run --reload

the --reload flag allows the server to automatically reload when changes are made to the app.

### TESTING

## Testing DATABASE Setup
You can load a dummy database to run the testing suite. From the project directory run:
psql movie_app_test < movie_app_test.sql

## Authentication Tokens
test_setup sets the tokens for authorization in environmental variables for the testing suite.
run:
source test_setup.sh

to export these variables before you run the testing suite and any time you need to change the tokens.

## test_app.py
this is the testing suite. it runs 18 tests. One for each endpoint success, one for each endpoint failure, and four to test roles permissions. To run make sure you setup the database with the dummy data and exported the token values as stated above. then run:
python test_app.py

## ERRORS
Request Errors are returned as JSON objects in the following format:

{
    "success": False,
    "error": 400,
    "message": "bad request"
}

The API will return three error types when the requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable

Authentication and Authorization Errors are also returned as JSON objects with a description of the error and the status code.

{
    "code": "authorization_header_missing",
    "description": "Authorization header is expected."
}

The API will also return three error types when the Authorization and Authentication fails:

400: Bad Request
401: Unauthorized
403: Forbidden

## ENDPOINTS
All endpoints require an authorization token and are limited to access by specific roles


GET /actors
    Returns a list of actors objects and success value
    Roles with Access include:
        Casting Director
        Casting Assistant
        Executive Producer

    Sample: curl --request GET 'https://movie-app-ak.herokuapp.com/actors' \
    --header 'Authorization: Bearer <TOKEN>

    {
        "actors": [
            {
                "id": 1,
                "name": "Harrison Ford",
                "birthdate": "1942-07-13",
                "gender": "Male"
            },
            {
                "id": 2,
                "name": "Carrie Fisher",
                "birthdate": "1942-07-13",
                "gender": "Female"
            }],
        "success": true
    }


GET /movies
    Returns a list of movies objects and success value
    Roles with Access include:
        Casting Director
        Casting Assistant
        Executive Producer

    Sample: curl --request GET 'https://movie-app-ak.herokuapp.com/movies' \
    --header 'Authorization: Bearer <TOKEN>

    {
        "movies": [
            {
                "id": 1,
                "name": "Blade Runner",
                "release": "1982-06-25"
            },
            {
                "id": 1,
                "name": "Star Wars",
                "release": "1982-06-25"
            }],
        "success": true
    }


POST /actors
    Adds an actor to the database and returns the actor object and success value
    Requires JSON object as body with values(name, birthdate, gender)
    Roles with access inclue:
        Casting Director
        Executive Producer

    Sample: curl --request POST 'https://movie-app-ak.herokuapp.com/actors' \
    --header 'Authorization: Bearer <TOKEN> \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "actor name",
        "birthdate": "yyyy-mm-dd",
        "gender": "gender"
    }'

    returns:
    {
        "actor": {
            "birthdate": "Mon, 13 Jul 1942 00:00:00 GMT",
            "gender": "Male",
            "id": 1,
            "name": "Harrison Ford"
        },
        "success": true
    }


POST /movies
    Adds a movie to the database and returns the movie object and success value
    Requires JSON object as body with values(title, release)
    Roles with access inclue:
        Executive Producer

    Sample: curl --request POST 'https://movie-app-ak.herokuapp.com/movies' \
    --header 'Authorization: Bearer <TOKEN> \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "title": "movie title",
        "release": "yyyy-mm-dd"
    }'

    returns:
    {
    "movie": {
        "id": 1,
        "release": "Fri, 25 Jun 1982 00:00:00 GMT",
        "title": "Blade Runner"
    },
    "success": true
}


PATCH /actors
    Updates actor information and returns the actor object and success value
    Requires actor id in the url and a JSON object as body
    Only the data being updated is required in the body
    Values can be (name, birthdate, gender)
    Roles with access include:
        Casting Director
        Executive Producer

    Sample: curl --request PATCH 'https://movie-app-ak.herokuapp.com/actors/<id>' \
    --header 'Authorization: Bearer <TOKEN> \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name": "actor name",
        "birthdate": "yyyy-mm-dd",
        "gender": "gender"
    }'

    Returns:
    {
    "actor": {
        "birthdate": "Mon, 13 Jul 1942 00:00:00 GMT",
        "gender": "GENDER",
        "id": 1,
        "name": "NAME"
    },
    "success": true
}


PATCH /movies
    Updates movie information and returns the movie object and success value
    Requires the movie id in the url and JSON object as body
    Only the data being updated is required in the body
    Value can be (title, release)
    Roles with access include:
        Casting Director
        Executive Producer

    Sample: curl --request PATCH 'https://movie-app-ak.herokuapp.com/movies/<id>' \
    --header 'Authorization: Bearer <TOKEN> \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "title": "movie title",
        "release": "yyyy-mm-dd"
    }'

    Returns:
    {
    "movie": {
        "id": 1,
        "release": "Fri, 25 Jun 1982 00:00:00 GMT",
        "title": "MOVIE TITLE"
    },
    "success": true
}


DELETE /actors
    Deletes an actor from the database
    Requires the actor id in url
    Returns the deleted actor id and the success value
    Roles with access inclue:
        Casting Director
        Executive Producer

    Sample: curl --request DELETE 'https://movie-app-ak.herokuapp.com/actors/<id>' \
    --header 'Authorization: Bearer <TOKEN>

    returns:
    {
    "delete": 1,
    "success": true
}


DELETE /movies
    Deletes a movie from the database
    Requires the movie ID in the url
    Returns the deleted movie id and the success value
    Roles with access inclue:
        Executive Producer

    Sample: curl --request DELETE 'https://movie-app-ak.herokuapp.com/movies/<id>' \
    --header 'Authorization: Bearer <TOKEN>

    returns:
    {
    "delete": 1,
    "success": true
}


## Temporary Tokens
Casting Assistant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiZDAwOTk1MTk3MDA2OGY5MjljOCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxODk1OTYsImV4cCI6MTYwNzI3NTk5NiwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.cd3i0N6G1ShR-pL4cDdQv-9YVjNANg1Zekbo-wDRk04YGO1jNQFGostTFMotFjOzSYqMoi0Rz9OMoG1BLA1sStOUmsHLs45gh6n-ku1Dd-T_OFlvdlBAoGCSWZaJpfc73cT77ukMrs0UKhbjyUSSrRw0pbkYaGzy4fxJDMfjFl2U7UIViiOUFergTjJJ8tGKAJePpmBKFTOt8Q2iC_FWpyFWQp_DpwCPGSECMqLw2PNhZ6tSF9eCjAJXLYvjBquDN9BNZsyMv4-PTqG-PupbS9hM4Sp7zAH9dEItvtVP_1M6XhsL5MzmJx9APg9ycN78gZALis1UVDpkit67x_WWog


Casting Director

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzZhMzQyMDI1NzBjMDA2ZTliMTU2MSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxODk1MTksImV4cCI6MTYwNzI3NTkxOSwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.rBs6o2lyNGDQMY9evb2pAdmRLO88bGo9gSSGnzg9zS3lNe7EKA-svgA4ZQEnPFcSq7ztfpwdbub_z04aiGxsOi05459XQ4_3ZtPY-zYqv_u9kg90EkblVVGMpFah4Fofziee7sqOfv9gWEr6QILZaHlbSJoPEpMH2gqt5L0h2yy3vlMk_pRyA1iMGKiLF1I4p2tT-d0w-kK_yBofN4E2Xgr9L4Dy_IwOi_esCHR6NA2co2GBdxdq3e6p0osZ62LcVc5yM2IvmvRE2fNcfTdDUldJWXUtCXNsSxidxXAmsT31WNUGbuyEV6C6YI_z6D5OP1iD6cjFqSICRjIEdAg6VQ


Executive Producer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiYjczOTk1MTk3MDA2OGY5MjhkZSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxOTgxNjQsImV4cCI6MTYwNzI4NDU2NCwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.ElcbXjT71ccEvYU5CazW59qo6T9zMYK_8Yo2ArdhmR9AmFR1BHf4OKj_KYG3lfo84zqo6OoM6Rn_CfHtjMLwTO8Cenr8YZZ3gNbTgHZBk8aOWEolZ43J8rzP7JC07NgKwZ7P2sFSPp8C8t9Sx1GsCuA7h_t3iORZD3IlGQ68QcUfD_WEnEw0cna1bjq3IAMArMMyJ7xhrNQk1JYXeUGyabrRzepoueH1_TPtZS1oOkbdB8UtFkZUifZaOJ7_GCWSTFsB95fi7OcUcDWpbp-VRNObXP5HrKu0a6Eg15Z4IAnKLUup-XBpSyCXMj1OaaPzQNXhwZLDJ0Iz2pe_Aeu8BQ