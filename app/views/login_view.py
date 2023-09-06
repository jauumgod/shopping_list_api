from ..schemas import login_schemas
from app import api
from flask_restful import Resource
from ..services.user_service import UserService
from ..models.user_model import UserModel
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import request, make_response, jsonify

class LoginListView(Resource):
    
    def post(self):
        LS = login_schemas.LoginSchema()
        validate = LS.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            usuario = request.json['usuario']
            senha = request.json['senha']

            usuario_bd = UserService.read_all(usuario)

            if usuario_bd and usuario_bd.decripto_senha(senha):
                access_token = create_access_token(
                    identity = usuario_bd.id,
                    expires_delta = timedelta(seconds=300)
                )
            refresh_token = create_refresh_token(
                identity= usuario_bd.id
            )
            return make_response(
                jsonify(
                {
                    'access_token' : access_token,
                    'refresh_token': refresh_token,
                    'mensagem': 'Login Realizado com sucesso!'
                }),200)
        
        return make_response(
            jsonify({'mensagem': 'credenciais invalidas'}), 400
        )

            
api.add_resource(LoginListView, "/login")