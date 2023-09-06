from flask_restful import Resource
from app import api
from ..schemas.history_schemas import HistorySchema
from ..services import history_service
from flask import request, make_response, jsonify, render_template, url_for
from app import app

class PaginaVazia(Resource):

    @app.route('/')
    def get():
        return render_template("index.html")
    

api.add_resource(PaginaVazia, '/')