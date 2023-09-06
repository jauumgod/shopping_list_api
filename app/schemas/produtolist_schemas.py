from app import ma
from ..models import produtolista_model
from marshmallow import fields

class ProdutoListSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = produtolista_model.ProdutoLista
        load_instance = True

    lista_id = fields.Integer(required=True)
    produto_id = fields.Integer(required=True)
    quantidade = fields.Integer(required=True)

    lista_id_key = fields.Integer(required=True)
    produto_id_key = fields.Integer(required=True)


