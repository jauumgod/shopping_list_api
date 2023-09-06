from app import db


class ProdutoLista(db.Model):
    __tablename__ = "tab_produtos_list"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    lista_id = db.Column(db.Integer)
    produto_id = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)

    lista_id_key = db.Column(db.Integer, db.ForeignKey('tab_shoppinglist.id'))
    produto_id_key = db.Column(db.Integer, db.ForeignKey('tab_produtos.id'))