from app import api, Resource, request, make_response, jsonify, date
from ..schemas import shoppinglist_schemas
from ..entities import shopping
from ..services import shoppinglist_service



class ShoppingListView(Resource):

    def get(self):
        shopping = shoppinglist_service.ShoppingListService.read()
        ss = shoppinglist_schemas.ShoppingListSchemas(many=True,only=("username","date_create"))
        return make_response(ss.jsonify(shopping), 201)

    def post(self):
        ss = shoppinglist_schemas.ShoppingListSchemas()
        validate = ss.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            username = request.json["username"]
            date_create = date.today()

            novo_shopping_list = shopping.Shopping(username=username, date_create=date_create)
            resultado = shoppinglist_service.ShoppingListService.create(novo_shopping_list)
            return make_response(ss.jsonify(resultado), 201)

api.add_resource(ShoppingListView, '/shoppinglist')