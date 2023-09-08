from ..models import produtolista_model
from ..models.produtolista_model import ProdutoLista



class ProdutoListService():

    def create(produtolist):
        create_produto_list = ProdutoLista(
            lista_id = produtolist.lista_id,
            produto_id = produtolist.produto_id,
            quantidade = produtolist.quantidade,
            lista_id_key = produtolist.lista_id_key,
            produto_id_key = produtolist.produto_id_key
        )
        create_produto_list.session.add()
        create_produto_list.session.commit()

    def read():
        query = ProdutoLista.query.all()
        return query