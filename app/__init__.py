from flask import Flask, url_for, request, redirect, make_response, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
import pymysql
from datetime import date, timedelta, datetime
from marshmallow import fields
from passlib.hash import pbkdf2_sha256

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mi = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)
jwt = JWTManager(app)

from .models import produtos_model, user_model, history_model, produtolista_model, shoppinglist_model
from .views import instrutions_page, produtos_view, user_view, history_view, login_view, shopping_list_view,produtos_list_view
