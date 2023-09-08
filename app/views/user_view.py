from app import api, Resource, request, make_response, jsonify
from ..schemas import user_schemas
from ..entities import user
from ..services import user_service
from ..errors_messages import errors


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
               return make_response(jsonify(errors.UserErrorMessages.USER_EXISTS), errors.StatusCode.STATUSCODE_422)


        
api.add_resource(UserListView, '/usuarios')