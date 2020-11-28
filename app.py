from flask import Flask, jsonify, request, abort
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth_decorator
import json

def create_app():

    app = Flask(__name__)
    setup_db(app)

    return app

app = create_app()


#ENDPOINTS

#MOVIES
@app.route('/movies', methods=['GET'])
@requires_auth_decorator
def get_movies(token):
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


@app.route('/movies/<int:id>', methods=['PATCH'])
def edit_movie(id):
    body = request.get_json()
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if movie is None:
        abort(404)
    else:
        if 'title' in body:
            movie.title = body.get('title')
        if 'release' in body:
            movie.release = body.get('release')
        try:
            movie.update()
            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except:
            abort(422)


@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if movie is None:
        abort(404)
    else:
        try:
            movie.delete()
            return jsonify({
                'success': True,
                'delete': id
            })
        except:
            abort(422)


#ACTORS
@app.route('/actors', methods=['GET'])
def get_actors():
    selection = Actor.query.all()
    actors = [actor.format() for actor in selection]
    return jsonify({
        'success': True,
        'actors': actors
    })


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


@app.route('/actors/<int:id>', methods=['PATCH'])
def update_actor(id):
    body = request.get_json()
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    if actor is None:
        abort(404)
    else:
        if 'name' in body:
            actor.name = body.get('name')
        if 'birthdate' in body:
            actor.birthdate = body.get('birthdate')
        if 'gender' in body:
            actor.gender = body.get('gender')
        try:
            actor.update()
            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except:
            abort(422)


@app.route('/actors/<int:id>', methods=['DELETE'])
def delete_actor(id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    if actor is None:
        abort(404)
    else:
        try:
            actor.delete()
            return jsonify({
                'success': True,
                'delete': id
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


#AuthError Handler
@app.errorhandler(AuthError)
def auth_error(AuthError):
    return jsonify(AuthError.error), AuthError.status_code


if __name__ == '__main__':
    app.run()