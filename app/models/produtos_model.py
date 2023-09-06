from app import db 


class ProdutosModel(db.Model):
    __tablename__ = 'tab_produtos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    quantidade = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

