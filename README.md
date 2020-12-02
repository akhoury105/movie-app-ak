# movie-app-ak

This is a simple API to access a Database of movies and actors. It was made as the capstone project for the FSND course at Udacity

## GETTING STARTED
 Base URL: https://movie-app-ak.herokuapp.com This App currently does not have a Frontend so there is nothing present at the base URL

 Authentication: Uses token Authentication. 
 Also has three roles which have access to specific endpoints:
    Casting Assistant
    Casting Director
    Executive Producer

Temporary tokens for each role are included at the end of the README.

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
    Returns a list of actors and success value
    Roles with Access include:
        Casting Director
        Casting Assistant
        Executive Producer

    Sample: curl --request GET 'https://movie-app-ak.herokuapp.com/actors' \
    --header 'Authorization: Bearer <TOKEN>

GET /movies
    Returns a list of movies and success value
    Roles with Access include:
        Casting Director
        Casting Assistant
        Executive Producer

    Sample: curl --request GET 'https://movie-app-ak.herokuapp.com/movies' \
    --header 'Authorization: Bearer <TOKEN>

POST /actors
    Adds an actor to the database and returns the actor object and success value
    Requires JSON object as body
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

POST /movies
    Adds a movie to the database and returns the movie object and success value
    Requires JSON object as body
    Roles with access inclue:
        Executive Producer

    Sample: curl --request POST 'https://movie-app-ak.herokuapp.com/movies' \
    --header 'Authorization: Bearer <TOKEN> \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "title": "movie title",
        "release": "yyyy-mm-dd"
    }'

PATCH /actors
    Updates actor information and returns the actor object and success value
    Requires JSON object as body
    Only the data being updated is required in the body
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

PATCH /movies
    Updates movie information and returns the movie object and success value
    Requires JSON object as body
    Only the data being updated is required in the body
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

DELETE /actors
    Deletes an actor from the database
    Returns the deleted actor id and the success value
    Roles with access inclue:
        Casting Director
        Executive Producer

    Sample: curl --request DELETE 'https://movie-app-ak.herokuapp.com/actors/<id>' \
    --header 'Authorization: Bearer <TOKEN>

DELETE /movies
    Deletes a movie from the database
    Returns the deleted movie id and the success value
    Roles with access inclue:
        Executive Producer

    Sample: curl --request DELETE 'https://movie-app-ak.herokuapp.com/movies/<id>' \
    --header 'Authorization: Bearer <TOKEN>



## Temporary Tokens
Casting Assistant


Casting Director


Executive Producer

