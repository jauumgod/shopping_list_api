DEBUG = True

USERNAME = 'jmnd1'
PASSWORD = 'A1h2q4v1'
SERVER = 'localhost'
DB = 'shopping_list'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'hesoyams2uzumymw'