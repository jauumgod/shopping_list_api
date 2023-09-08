from ..models import produtolista_model
from ..models.produtolista_model import ProdutoLista
from app import db


class ProdutoListService():

    def create(produtolist):
        create_produto_list = ProdutoLista(
            lista_id = produtolist.lista_id,
            produto_id = produtolist.produto_id,
            quantidade = produtolist.quantidade,
            lista_id_key = produtolist.lista_id_key,
            produto_id_key = produtolist.produto_id_key
        )
        db.session.add(create_produto_list)
        db.session.commit()
        return True

    def read():
        query = ProdutoLista.query.all()
        return query