from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.lista_model import ListaModel
from lista.models.item_lista_model import ItemLista
from lista.models.item_model import ItemModel
#from lista.schemas.schemas import ListaSchema
from lista.schemas.lista_schema import ListaSchema

class ListaResource (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("itens",
                        type=dict, location='json', action='append',
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do Item não pode estar em branco."
                        )
    def post(self):
        json = ''
        try:
            data = ListaResource.parser.parse_args()
            if not data:
                return {"mensagem": "A requisição não tem dados JSON"}, 400
            lista = ListaModel.encontrar_pelo_nome(nome=data["nome"])
            if lista:
                return {"mensagem": "Uma lista já existe com esse nome"}, 400

            itens_lista = data['itens']
            nome = data['nome']
            lista = ListaModel(nome=nome,usuario_id=1)

            for i in itens_lista:
                il =ItemLista(preco="20 reais")
                item_temp = ItemModel.encontrar_pelo_nome(i['nome'])
                if item_temp:
                    il.item = item_temp
                else:
                    il.item = ItemModel(nome=i['nome'])
                lista.itens.append(il)
            lista.adicionar()
            lista = ListaModel.encontrar_pelo_nome(data["nome"])
            schema = ListaSchema()
            json = schema.dump(lista).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def get(self,nome):
        json = ""
        try:
            item = ListaModel.encontrar_pelo_nome(nome)
            if item:
                schema = ItemSchema(many=False)
                json = schema.dump(item).data
            else:
                abort(404, message="Item {} não está na lista".format(item))
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(item))
            
class ListasResource(Resource):

    def get(self):
        json = ""
        try:
            listas = ListaModel.listar()
            schema = ListaSchema(many=True)
            json = schema.dump(listas).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json, 200