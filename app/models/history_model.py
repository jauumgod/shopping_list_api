from app import db, datetime


class HistoryModel(db.Model):
    __tablename__ = 'tab_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    produto_id = db.Column(db.Integer)
    quantidade_id = db.Column(db.Integer)
    data_compra = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    usuario_id_key = db.Column(db.Integer, db.ForeignKey('tab_usuarios.id'))
    produto_id_key = db.Column(db.Integer, db.ForeignKey('tab_produtos.id'))
    