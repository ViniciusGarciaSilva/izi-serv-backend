from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.cliente_model import ClienteModel
from lista.schemas.cliente_schema import ClienteSchema

class ClienteResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do Cliente não pode estar em branco."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="O email do Cliente não pode estar em branco."
                        )

    def get(self,nome):
        json = ''
        try:
            nome = ClienteModel.encontrar_pelo_id(nome)
            if nome:
                schema = ClienteSchema()
                json = schema.dump(nome).data
            else:
                abort(404, message="Cliente {} não está na lista".format(nome))
        except Exception as e:
            print(e)
            abort(404, message="Cliente {} não está na lista".format(nome))

        return json,201


    def post(self):
        json = ''
        try:
            data = ClienteResource.parser.parse_args()
            print(data)
            nome = data['nome']
            email = data['email']
            cliente = ClienteModel.encontrar_pelo_nome(nome)
            if cliente :
                return {"message":"Cliente {} já está na lista".format(nome)}
            else:
                cliente = ClienteModel(nome=nome, email=email)
                cliente.adicionar()
                cliente = ClienteModel.encontrar_pelo_nome(nome)
                schema = ClienteSchema()
                json = schema.dump(cliente).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,nome):
        json = []
        try:
            nome = ClienteModel.encontrar_pelo_id(nome)
            if nome:
                nome.remover()
                lista = ClienteModel.listar()
                schema = ClienteSchema(many=True)
                json = schema.dump(lista).data
            else:
                return {"message":"Cliente {} não está na lista".format(nome)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = ClienteResource.parser.parse_args()
            nome = data['cliente']

            cliente = ClienteModel.encontrar_pelo_nome(nome)
            if cliente :
                return {"message":"Cliente {} já está na lista".format(cliente)},200
            else:
                cliente = ClienteModel(nome=nome, email=email)
                cliente.adicionar()
                schema = ClienteSchema(many=True)
                cliente = ClienteModel.encontrar_pelo_nome(nome)
                json = schema.dump(cliente).data
        except Exception as e:
            print(e)
        return json, 201

class ClientesResource(Resource):
    def get(self):
        json = []
        try:
            itens = ClienteModel.listar()
            schema = ClienteSchema(many=True)
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201