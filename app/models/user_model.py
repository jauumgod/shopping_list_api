from app import db, pbkdf2_sha256



class UserModel(db.Model):
    __tablename__ = 'tab_usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(255), nullable=False)


    def cripto_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def decripto_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
    