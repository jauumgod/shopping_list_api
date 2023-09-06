from datetime import datetime
from app import db

class ShoppingList(db.Model):
    __tablename__ = "tab_shoppinglist"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.Integer)
    date_create = db.Column(db.TIMESTAMP, default=datetime.utcnow)


    def __init__(self, username, date_create):
        self.username = username
        self.date_create = date_create