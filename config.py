import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Give access to the project in ANY OS we find ourselves in
# Allow outside files/folders to be added to the project from the
#Base directory

class Config():
    """
        Set config variables for the flask app.
        Using Environment variables where available otherwise
        create the config variables if not done already.
    """
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thisiswherepassgoes@127.0.0.1:5432/car_collection'
    SQLALCHEMY_TRACK_MODIFICATIONS=False # Turn off update messages from the sqlalchemy