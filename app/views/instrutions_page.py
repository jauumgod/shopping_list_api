from ..schemas.history_schemas import HistorySchema
from ..services import history_service
from app import app, request, make_response, jsonify, render_template, url_for, api, Resource

class PaginaVazia(Resource):

    @app.route('/')
    def get():
        return render_template("index.html")
    

api.add_resource(PaginaVazia, '/')