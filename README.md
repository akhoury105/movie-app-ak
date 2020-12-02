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

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiZDAwOTk1MTk3MDA2OGY5MjljOCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDY5MzQ0NjEsImV4cCI6MTYwNzAyMDg2MSwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.QAiYR47g90xuMk8ueVyuuri9nbZSCNZjdCwequxsaPLtlKiwghPtQDF-qeZs8sld9r-rygIOjeIPhbYD81r8DhIjXauYu-yLWrdCPt6ROLG8YHvOnLk_MrzR6mtG2gxGlVAH33fHj-9NeTMcoDjzNocHLln8dUUhQ98AiNUIbf16J7rEvAY9BH344rrcU4AUrIifZu0LU_iUmAd5Jr0P1ZMrk-OoUCx-0oCOVpJcNi7M8gzMl-OQHC860IqNwJ_Y81-XD00o6Ee_YW0KLOsJ0LWdMHQ-u_SgIZxkdsviEtqQJQQYwoRLgV78WDKW9IGimyz7bW7_FdNN-U8LXtEcNw


Casting Director

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzZhMzQyMDI1NzBjMDA2ZTliMTU2MSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDY5MzQ3MDIsImV4cCI6MTYwNzAyMTEwMiwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.NPjj9nqWUZsulOCtJy2jvVZNAEo4vKkclKcZOS0QWW1dSYA0tOBbf19Y44xuWQ4UmMTZmE7__DPBuCJgVoqP_maBEQvXZ8aXuvMhIx3nvf54qIBm-81DeCHK4sbTQ3iEU7oXo4JK1eI12eaY3DCL7OexqZ52LEZwcvq48jI3ZOssxpgjy82HlL_HEs7jBqxw-kKB6rJCQkWRYhJT8Oq8mt5druNansFYlExok1UYALh3OlMtVfVcRlCDvFlLeQzG8dU9b3JrFB5_blRxmCte_3cj8g3cYuLJSQtEuYceqbCmgo7jsUlkkixoJGGUWn3OY39CjH0iV64OIPB6V0PpHg


Executive Producer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiYjczOTk1MTk3MDA2OGY5MjhkZSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDY5MzQzMTYsImV4cCI6MTYwNzAyMDcxNiwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.rehupumxgD_TaLDq7SvzQWzF7pSOuyoN2H-T28sPPBO2wKiOZU99fuFAr4VKe5k8gJ6QTDeuZ6sZJgZHh6cUp1lWpCnn7Nja07FaxYElcSEpbmTPrxPWA_JOPbOmRhHggzBIkR-8LPC6zELZVyE4eAwh096rWZ_DIGcwKc897u0STbBwaaB75wH-Oq2Ln4UhU3DP--qBoDlPx34evPdc4UPuG0F5dXOqBB-SEU2dSOqQHujr8pKJsGZTiHVAUk3CEkEyXCN-hPbRVfLQsLDojWyq8GZlQDh1NdGpXVYSxkc4m1ldOkXWfZ4GzWBht-gQEQJGIir8yhExyfYHQ_Q7EQ