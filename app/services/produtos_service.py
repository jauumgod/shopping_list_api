from app import db
from ..models import produtos_model
from ..models.produtos_model import ProdutosModel


class ProdutosService():

    def create(item):
        create_item = ProdutosModel(nome = item.nome, quantidade=item.quantidade)
        db.session.add(create_item)
        db.session.commit()

    def read_all():
        all = produtos_model.ProdutosModel.query.all()
        return all

    def read_with_id(id):
        filter = ProdutosModel.query.filter_by(id=id).first()
        return filter
    
    def update(id, new_name):
        ProdutosModel.query.filter_by(id=id).update({'nome': f'{new_name}'})
        db.session.commit()


    def delete_data(id):
        data = ProdutosModel.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()


    