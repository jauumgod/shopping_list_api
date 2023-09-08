from app import ma, fields

from app.models import shoppinglist_model


class ShoppingListSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = shoppinglist_model.ShoppingList
        load_instance = True

    username = fields.Integer(required=True)
    date_create = fields.Date(required=False)
