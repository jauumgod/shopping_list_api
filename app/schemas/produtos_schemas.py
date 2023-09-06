from app import ma
from ..models import produtos_model
from marshmallow import fields


class ProdutosSchemas(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = produtos_model.ProdutosModel
        load_instance = True



    nome = fields.String(required=True)
    quantidade = fields.Integer(required=True)
