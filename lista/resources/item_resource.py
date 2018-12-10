from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.item_model import ItemModel
from lista.models.item_lista_model import ItemLista
from lista.schemas.item_schema import ItemSchema

class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item',
                        type=str,
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )

    def get(self,item):
        json = ''
        try:
            item = ItemModel.encontrar_pelo_nome(item)
            if item:
                schema = ItemSchema(exclude=['listas'])
                json = schema.dump(item).data
            else:
                abort(404, message="Item {} não está na lista".format(item))
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(item))

        return json,201


    def post(self):
        json = ''
        try:
            data = ItemResource.parser.parse_args()
            print(data)
            nome = data['item']
            item = ItemModel.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(nome)}
            else:
                item = ItemModel(nome=nome)
                item.adicionar()
                item = ItemModel.encontrar_pelo_nome(nome)
                schema = ItemSchema(exclude=['listas'])
                json = schema.dump(item).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,item):
        json = []
        try:
            item = ItemModel.encontrar_pelo_nome(item)
            if item:
                item.remover()
                lista = ItemModel.listar()
                schema = ItemSchema(many=True,exclude=['listas'])
                json = schema.dump(lista).data
            else:
                return {"message":"Item {} não está na lista".format(item)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = ItemResource.parser.parse_args()
            nome = data['item']

            item = ItemModel.encontrar_pelo_nome(nome)
            if item :
                return {"message":"Item {} já está na lista".format(item)},200
            else:
                item = ItemModel(nome=nome)
                item.adicionar()
                schema = ItemSchema(many=True)
                item = ItemModel.encontrar_pelo_nome(nome)
                json = schema.dump(item).data
        except Exception as e:
            print(e)
        return json, 201

class ItensResource(Resource):
    def get(self):
        json = []
        try:
            itens = ItemModel.listar()
            schema = ItemSchema(many=True,exclude=['listas'])
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201