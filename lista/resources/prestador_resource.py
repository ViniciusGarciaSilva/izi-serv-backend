from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.prestador_model import PrestadorModel
from lista.schemas.prestador_schema import PrestadorSchema

class PrestadorResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do Prestador não pode estar em branco."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="O email do Prestador não pode estar em branco."
                        )

    def get(self,nome):
        json = ''
        try:
            nome = PrestadorModel.encontrar_pelo_id(nome)
            if nome:
                schema = PrestadorSchema()
                json = schema.dump(nome).data
            else:
                abort(404, message="Prestador {} não está na lista".format(nome))
        except Exception as e:
            print(e)
            abort(404, message="Prestador {} não está na lista".format(nome))

        return json,201


    def post(self):
        json = ''
        try:
            data = PrestadorResource.parser.parse_args()
            print(data)
            nome = data['nome']
            email = data['email']
            prestador = PrestadorModel.encontrar_pelo_nome(nome)
            if prestador :
                return {"message":"Prestador {} já está na lista".format(nome)}
            else:
                prestador = PrestadorModel(nome=nome, email=email)
                prestador.adicionar()
                prestador = PrestadorModel.encontrar_pelo_nome(nome)
                schema = PrestadorSchema()
                json = schema.dump(prestador).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,nome):
        json = []
        try:
            nome = PrestadorModel.encontrar_pelo_id(nome)
            if nome:
                nome.remover()
                lista = PrestadorModel.listar()
                schema = PrestadorSchema(many=True)
                json = schema.dump(lista).data
            else:
                return {"message":"Prestador {} não está na lista".format(nome)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = PrestadorResource.parser.parse_args()
            nome = data['nome']
            email = data['email']

            prestador = PrestadorModel.encontrar_pelo_nome(nome)
            if prestador :
                return {"message":"Prestador {} já está na lista".format(prestador)},200
            else:
                prestador = PrestadorModel(nome=nome, email=email)
                prestador.adicionar()
                schema = PrestadorSchema(many=True)
                prestador = PrestadorModel.encontrar_pelo_nome(nome)
                json = schema.dump(prestador).data
        except Exception as e:
            print(e)
        return json, 201

class PrestadoresResource(Resource):
    def get(self):
        json = []
        try:
            itens = PrestadorModel.listar()
            schema = PrestadorSchema(many=True)
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201