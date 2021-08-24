# -*- coding: utf-8 -*-
''' 
flask_restplus swagger api with a Token based authentication (simple implementation), access the endpoint with /api/swagger/
The token function will be applied on all functions of the namespace ,we add @doc() function above the class for all methods and above method to lock a specific endpoint
'''
# Librarys
from flask import Flask, json, jsonify,request,abort, redirect, url_for
from flask_restplus import Resource, Api
from functools import wraps


# Variables
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'

authorizations = {
    'api_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-auth'
    },
}

def token_required(f):
    '''decorator function to check tokens in header'''
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'x-auth' not in request.headers:
            abort(400, 'Token is missing !')
        elif request.headers.get('x-auth') != "s3cret" :
            abort(400, 'Invalid token, an unauthorized access to the requested ressources.')
        return f(*args, **kwargs)
    return wrapped

#Initialize the api functions
api = Api(app,title='Books Store Rest API',version='v0.1',doc='/api/swagger/')
books_swagger = api.namespace('Books', description='Operations related to books',authorizations=authorizations,security='api_token',decorators=[token_required])


@books_swagger.route('/')
@api.doc(security='api_token')
class BooksCollection(Resource):
    def get(self):
        """ Return a list of books """
        return jsonify(["CULT OF THE DEAD COW","PRACTICAL MALWARE ANALYSIS","THE CYBER EFFECT"])
    
    def post(self):
        """ Add a new book to database"""
        return jsonify({"messgae":"function not implemented yet:"})
        
# Run
if __name__ == '__main__':
    app.run()
