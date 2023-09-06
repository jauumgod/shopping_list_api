
from flask_restful import Resource
from app import api
from ..schemas.history_schemas import HistorySchema
from ..services import history_service
from ..entities import historico
from flask import request, make_response, jsonify

from datetime import date



class HistoryViewList(Resource):

    def get(self):
        items = history_service.HistoricService.read_all()
        HS = HistorySchema(many=True)
        return make_response(HS.jsonify(items), 201)
    
    def post():
        hs = HistorySchema()
        validate = hs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            id = request.json["id"]
            data = date.today()
            print(id, data)

            save_history = historico.HistoryChanges(id=id, data=data)
            
            resultado = history_service.HistoricService.save_history(save_history)
            return make_response(hs.jsonify(resultado), 201)
            
    

api.add_resource(HistoryViewList, '/history')