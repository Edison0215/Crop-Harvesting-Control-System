#Identify file "websites" as a python package

from flask import Flask
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)  #Create a Flask application instance
    app.secret_key = "abc" #Set a secret key for the application

    #Import and register the 'views' and 'auth' blueprints
    from .views import views
    from .man import man
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(man, url_prefix='/')

    #Import the Use model
    from .models import User
    
    #Initialize the LoginManager
    login_manager = LoginManager()
    #Set the login view for the LoginManager
    login_manager.login_view = 'auth.login'
    # Initialize the LoginManager with the Flask app
    login_manager.init_app(app)

    # Define a user loader function for the LoginManager
    @login_manager.user_loader
    def load_user(id):
        return User.get(int(id))

    # Return the Flask app instance
    return app