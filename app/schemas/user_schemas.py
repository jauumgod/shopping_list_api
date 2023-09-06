from app import ma
from ..models import user_model
from marshmallow import fields

class UserSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.UserModel
        load_instance = True

    nome = fields.String(required=True)
    senha = fields.String(required=True)
