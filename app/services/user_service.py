from app import db
from flask import make_response, jsonify
from ..models import user_model
from ..models.user_model import UserModel
from ..errors import erros


class UserService():

    def create(usuario):
        query = UserModel.query.filter_by(nome=usuario.nome).first()
        if query.nome == usuario.nome:
            return make_response(jsonify(erros.UserErrorMessages.USER_EXISTS), erros.StatusCode.STATUSCODE_409)
        else:
            create_data = UserModel(nome=usuario.nome, senha = usuario.senha)
            create_data.cripto_senha()
            db.session.add(create_data)
            db.session.commit()


    def read_all():
        all = user_model.UserModel.query.all()
        return all
    
    def listar_usuario_id(id):
        usuario = user_model.UserModel.query.filter_by(id=id).first()
        return usuario
        
    def update_data(id, data_att):
        user_model.UserModel.query.filter_by(id=id).update({'nome': f'{data_att}'})
        db.session.commit()


    def delete_data(id):
        data = user_model.UserModel.query.filter_by()
        db.session.delete(data)
        db.session.commit()


    