from flask import Flask, jsonify, request, abort
from models import setup_db, Movie, Actor
import json

def create_app():

    app = Flask(__name__)
    setup_db(app)

    return app

app = create_app()


#ENDPOINTS
@app.route('/movies', methods=['GET'])
def get_movies():
    selection = Movie.query.all()
    movies = [movie.format() for movie in selection]
    return jsonify({
        'success': True,
        'movies': movies
    })

@app.route('/movies', methods=['POST'])
def add_movies():
    body = {}
    body = request.get_json()
    if not body:
        abort(404)
    title = body.get('title')
    release = body.get('release')
    movie = Movie(title=title, release=release)
    try:
        movie.insert()

        return jsonify({
            'success': True,
            'movie': movie.format()
        })
    except:
        abort(422)


@app.route('/actors', methods=['POST'])
def post_actor():
    body = {}
    body = request.get_json()
    if not body:
        abort(404)
    name = body.get('name')
    birthdate = body.get('birthdate')
    gender = body.get('gender')
    actor = Actor(name=name, birthdate=birthdate, gender=gender)
    try:
        actor.insert()

        return jsonify({
            'success': True,
            'actor': actor.format()
        })
    except:
        abort(422)


#ERROR HANDLERS
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    })


if __name__ == '__main__':
    app.run()