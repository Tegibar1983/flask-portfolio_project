from flask import flask

define create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!tagi'
    
    return app