from flask import g
from flask_restplus import Namespace, Resource

from erhi.models import auth

api = Namespace('login', description='user login')


@api.route('/')
class Login(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()

        return {
            'id': str(g.user.id),
            'username': g.user.username,
            'token': token.decode()
        }
