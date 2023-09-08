
from app import ma, fields
from ..models import user_model


class LoginSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = user_model.UserModel
        load_instance = True
        fields = ("id", "nome", "senha")


    nome = fields.String(required=True)
    senha = fields.String(required=True)
