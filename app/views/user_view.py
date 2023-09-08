from flask_restful import Resource
from app import api
from ..schemas import user_schemas
from flask import request, make_response, jsonify
from ..entities import user
from ..services import user_service
from ..errors import erros


class UserListView(Resource):

    def get(self):
        usuarios = user_service.UserService.read_all()
        us = user_schemas.UserSchemas(many=True, only=("nome", "id"))
        return make_response(us.jsonify(usuarios), 201)
        
    
    def post(self):
        us = user_schemas.UserSchemas()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            senha = request.json["senha"]
            usuario_novo = user.User(nome=nome, senha=senha)
            
            print(usuario_novo.nome, usuario_novo.senha)
            resultado = user_service.UserService.create(usuario_novo)
            if resultado == True:
                return make_response(us.jsonify(resultado), 201)
            else:
               return make_response(jsonify(erros.UserErrorMessages.USER_EXISTS), erros.StatusCode.STATUSCODE_422)


        
api.add_resource(UserListView, '/usuarios')