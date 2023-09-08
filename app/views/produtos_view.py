from app import api, Resource, request, make_response, jsonify
from ..schemas import produtos_schemas
from ..services  import produtos_service
from ..entities import produtos
from ..errors_messages import errors


class ItemViewList(Resource):

    def get(self):
        items = produtos_service.ProdutosService.read_all()
        IS = produtos_schemas.ProdutosSchemas(many=True, only=("id", "nome", "quantidade"))
        return make_response(IS.jsonify(items), 201)
    
    def post(self):
        IS = produtos_schemas.ProdutosSchemas()
        validate = IS.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        
        else:
            nome = request.json['nome']
            quantidade = request.json['quantidade']
            novo_item = produtos.Produtos(nome=nome, quantidade=quantidade)

            print(f"meu print: {novo_item.nome, novo_item.quantidade}")
            resultado = produtos_service.ProdutosService.create(novo_item)
            if resultado == True:
                return make_response(IS.jsonify(resultado), 201)
            else:
                return make_response(jsonify(errors.ItemErrorMessages.ITEM_EXISTS),errors.StatusCode.STATUSCODE_422)



class ItemViewDetails(Resource):

    def get(self,id):
        item = produtos_service.ProdutosService.read_with_id(id)
        IS =produtos_schemas.ProdutosSchemas()
        return make_response(IS.jsonify(item), 200)


    def put(self, id):
        conta_bd = produtos_service.ProdutosService.read_with_id(id)
        IS = produtos_schemas.ProdutosSchemas()
        validate = IS.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            nome = request.json["nome"]
            quantidade = request.json["quantidade"]
            nova_conta = produtos.Items(nome=nome, quantidade=quantidade)
            resultado = produtos_service.ProdutosService.update(conta_bd, nova_conta)
            return make_response(IS.jsonify(resultado), 201)

    def delete(self,id):
        item = produtos_service.ProdutosService.read_with_id(id)
        produtos_service.ProdutosService.delete(item)
        return make_response(jsonify(""), 204)


api.add_resource(ItemViewList, '/products')
api.add_resource(ItemViewDetails, '/products/<int:id>')