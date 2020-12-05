import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


assistant_token = os.environ['ASSISTANT_TOKEN']
director_token = os.environ['DIRECTOR_TOKEN']
producer_token = os.environ['PRODUCER_TOKEN']

class MovieAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movie_app_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.cast_ast = assistant_token
        self.cast_dir = director_token
        self.exec_prod = producer_token
        self.headers = {'Authorization':
                        'Bearer ' + self.exec_prod}

    def tearDown(self):
        pass

    '''
    Tests for all endpoints
    These use an Executice Producer Token for authorization

    '''

    def test_get_movies(self):
        res = self.client().get('/movies',
                                headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors(self):
        res = self.client().get('/actors',
                                headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movie(self):
        self.new_movie = {
            "title": "Blade Runner",
            "release": "1982-06-25"
        }
        res = self.client().post('/movies',
                                 headers=self.headers,
                                 json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_body_not_found_posting_movie(self):
        res = self.client().post('/movies',
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_actor(self):
        self.new_actor = {
            "name": "Harrison Ford",
            "birthdate": "1942-07-13",
            "gender": "Male"
        }
        res = self.client().post('/actors',
                                 headers=self.headers,
                                 json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_body_not_found_posting_actor(self):
        res = self.client().post('/actors',
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/5',
                                   headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 5)

    def test_no_movie_to_delete(self):
        res = self.client().delete('/movies/1000',
                                   headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/5',
                                   headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 5)

    def test_no_actor_to_delete(self):
        res = self.client().delete('/actor/1000',
                                   headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_movie(self):
        self.movie_edit = {
            "title": "Star Wars"
        }
        res = self.client().patch('/movies/2',
                                  headers=self.headers,
                                  json=self.movie_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_no_movie_to_update(self):
        self.movie_edit = {
            "title": "Star Wars"
        }
        res = self.client().patch('/movies/1000',
                                  headers=self.headers,
                                  json=self.movie_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_actor(self):
        self.actor_edit = {
            "name": "Mark Hamill"
        }
        res = self.client().patch('/actors/3',
                                  headers=self.headers,
                                  json=self.actor_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_no_actor_to_update(self):
        self.actor_edit = {
            "name": "Mark Hamill"
        }
        res = self.client().patch('/actors/1000',
                                  headers=self.headers,
                                  json=self.actor_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Authorization testing for the Casting Director

    def test_casting_director_post_actor(self):
        self.new_actor = {
            "name": "Carrie Fisher",
            "birthdate": "1956-10-21",
            "gender": "Female"
        }
        res = self.client().post('/actors',
                                 headers={'Authorization':
                                          'Bearer ' + self.cast_dir},
                                 json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_unauth_movie_post_casting_director(self):
        self.new_movie = {
            "title": "Blade Runner",
            "release": "1982-06-25"
        }
        res = self.client().post('/movies',
                                 headers={'Authorization':
                                          'Bearer ' + self.cast_dir},
                                 json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    # Auth testing for Casting Assistant

    def test_casting_assistant_get_movie(self):
        res = self.client().get('/actors',
                                headers={'Authorization':
                                         'Bearer ' + self.cast_ast})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_unauth_movie_post_casting_assistant(self):
        self.new_movie = {
            "title": "Blade Runner",
            "release": "1982-06-25"
        }
        res = self.client().post('/movies',
                                 headers={'Authorization':
                                          'Bearer ' + self.cast_ast},
                                 json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')


if __name__ == "__main__":
    unittest.main()
