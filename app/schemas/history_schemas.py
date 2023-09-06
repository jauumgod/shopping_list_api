
from app import ma
from ..models import history_model
from marshmallow import fields


class HistorySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = history_model.HistoryModel
        load_instance = True
        include_fk= True

        nome = fields.String(required=True)
        data = fields.Date(required=True)