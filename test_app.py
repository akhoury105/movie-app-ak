import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie


class MovieAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movie_app_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.cast_ast = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiZDAwOTk1MTk3MDA2OGY5MjljOCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxODk1OTYsImV4cCI6MTYwNzI3NTk5NiwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.cd3i0N6G1ShR-pL4cDdQv-9YVjNANg1Zekbo-wDRk04YGO1jNQFGostTFMotFjOzSYqMoi0Rz9OMoG1BLA1sStOUmsHLs45gh6n-ku1Dd-T_OFlvdlBAoGCSWZaJpfc73cT77ukMrs0UKhbjyUSSrRw0pbkYaGzy4fxJDMfjFl2U7UIViiOUFergTjJJ8tGKAJePpmBKFTOt8Q2iC_FWpyFWQp_DpwCPGSECMqLw2PNhZ6tSF9eCjAJXLYvjBquDN9BNZsyMv4-PTqG-PupbS9hM4Sp7zAH9dEItvtVP_1M6XhsL5MzmJx9APg9ycN78gZALis1UVDpkit67x_WWog'
        self.cast_dir = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmYzZhMzQyMDI1NzBjMDA2ZTliMTU2MSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxODk1MTksImV4cCI6MTYwNzI3NTkxOSwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.rBs6o2lyNGDQMY9evb2pAdmRLO88bGo9gSSGnzg9zS3lNe7EKA-svgA4ZQEnPFcSq7ztfpwdbub_z04aiGxsOi05459XQ4_3ZtPY-zYqv_u9kg90EkblVVGMpFah4Fofziee7sqOfv9gWEr6QILZaHlbSJoPEpMH2gqt5L0h2yy3vlMk_pRyA1iMGKiLF1I4p2tT-d0w-kK_yBofN4E2Xgr9L4Dy_IwOi_esCHR6NA2co2GBdxdq3e6p0osZ62LcVc5yM2IvmvRE2fNcfTdDUldJWXUtCXNsSxidxXAmsT31WNUGbuyEV6C6YI_z6D5OP1iD6cjFqSICRjIEdAg6VQ'
        self.exec_prod = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1USy1QUklCLUNQalhMMXFtM1hTWSJ9.eyJpc3MiOiJodHRwczovL2Rldi1jb24udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmOTFiYjczOTk1MTk3MDA2OGY5MjhkZSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDcxMjQ1NjYsImV4cCI6MTYwNzIxMDk2NiwiYXpwIjoiQUhXVEtMZzQ4c1JaU0ZXMm5MVlhhc01VSFVyVTduRWUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.FoUtybbZNacSKnT5mBXPU9mFl58W_rTY8Xgary6cQy5Ue1o4b3rDcAW1KLH4fGrmx_Q88pxkyz3XCMJ3bENpArgpe-eRvFUlSXgjvyUbXr4LFhj5hk8P_V_fuJynAKsB2Is__-vO0pCn3mXkXKwY9DisGB4Y0E_94jUNKy59QvcwfWTKpG0667DdU7z2LkEbBODTa0CnOxE_GJW_c0FXqzRwI7TxreqDXPb1SX4EXtBH0ZfukWUzq16zYQ8Ou5kA48vl4ix9RfrYG85xJNK709btOIy-J3cY-w5X8FZ-kfOawQO5_eV2dI7MDJYb1xELFI9HKCNlEFbSQwDio6vsOA'
        self.headers = {'Authorization':
                'Bearer ' +self.exec_prod}


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
        res = self.client().delete('/movies/1',
                                    headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)


    def test_no_movie_to_delete(self):
        res = self.client().delete('/movies/1000',
                                    headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_delete_actor(self):
        res = self.client().delete('/actors/1',
                                    headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)


    def test_no_actor_to_delete(self):
        res = self.client().delete('/actor/1000',
                                    headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_patch_movie(self):
        self.movie_edit = {
            "title" : "Star Wars"
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
            "title" : "Star Wars"
        }
        res = self.client().patch('/movies/1000',
                                    headers=self.headers,
                                    json=self.movie_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_patch_actor(self):
        self.actor_edit = {
            "name" : "Mark Hamill"
        }
        res = self.client().patch('/actor/2',
                                    headers=self.headers,
                                    json=self.actor_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])


    def test_no_actor_to_update(self):
        self.actor_edit = {
            "name" : "Mark Hamill"
        }
        res = self.client().patch('/actors/1000',
                                    headers=self.headers,
                                    json=self.actor_edit)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    #Authorization testing for the Casting Director
    def test_casting_director_post_actor(self):
        self.new_actor = {
            "name": "Carrie Fisher",
            "birthdate": "1956-10-21",
            "gender": "Female"
        }
        res = self.client().post('/actors',
                                headers={'Authorization':
                                        'Bearer ' +self.cast_dir},
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
                                        'Bearer ' +self.cast_dir},
                                json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')


    #Auth testing for Casting Assistant
    def test_casting_assistant_get_movie(self):
        res = self.client().get('/actors',
                                headers={'Authorization':
                                        'Bearer ' +self.cast_ast})
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
                                        'Bearer ' +self.cast_ast},
                                json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')



if __name__ == "__main__":
    unittest.main()
