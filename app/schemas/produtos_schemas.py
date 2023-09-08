from app import ma, fields
from ..models import produtos_model



class ProdutosSchemas(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = produtos_model.ProdutosModel
        load_instance = True



    nome = fields.String(required=True)
    quantidade = fields.Integer(required=True)
