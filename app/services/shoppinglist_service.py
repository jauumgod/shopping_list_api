from app import db, date
from ..models import shoppinglist_model
from ..models.shoppinglist_model import ShoppingList

class ShoppingListService():

    def create(shoppinglist):
        create_shopping_list = ShoppingList(username = shoppinglist.username, date_create= shoppinglist.date_create)
        db.session.add(create_shopping_list)
        db.session.commit()
        return True

    def read():
        query = ShoppingList.query.all()
        return query
