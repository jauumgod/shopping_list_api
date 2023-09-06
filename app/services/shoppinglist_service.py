from app import db
from ..models import shoppinglist_model
from ..models.shoppinglist_model import ShoppingList

class ShoppingListService():

    def create(shoppinglist):
        create_shopping_list = ShoppingList(username = shoppinglist.username, date_create= shoppinglist.date_create)
        create_shopping_list.session.add()
        create_shopping_list.session.commit()

    def read():
        query = ShoppingList.query.all()
        return query
