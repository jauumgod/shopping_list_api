from flask_restful import Resource
from app import api
from ..schemas import produtolist_schemas
from flask import request, make_response, jsonify
from ..entities import produto_lista
from ..services import produtolist_service


class ProdutosListView(Resource):

    def get(self):
        shopping = produtolist_service.ProdutoListService.read()
        ss = produtolist_schemas.ProdutoListSchema(many=True,only=("produto_id","quantidade"))
        return make_response(ss.jsonify(shopping), 201)

    def post(self):
        ss = produtolist_schemas.ProdutoListSchema()
        validate = ss.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            lista_id = request.json["lista_id"]
            produto_id = request.json["produto_id"]
            quantidade = request.json["quantidade"]
            lista_id_key = request.json["lista_id_key"]
            produto_id_key = request.json["produto_id_key"]

            novo_produto_list = produto_lista.ProdutoLista(
                lista_id=lista_id,
                produto_id=produto_id,
                quantidade=quantidade,
                lista_id_key=lista_id_key,
                produto_id_key=produto_id_key)
            resultado = produtolist_service.ProdutoListService.create(novo_produto_list)
            return make_response(ss.jsonify(resultado), 201)

api.add_resource(ProdutosListView, '/produtoslistview')