from app import ma, fields
from ..models import user_model


class UserSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.UserModel
        load_instance = True

    nome = fields.String(required=True)
    senha = fields.String(required=True)
