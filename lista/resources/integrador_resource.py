from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.integrador_model import IntegradorModel
from lista.schemas.integrador_schema import IntegradorSchema

class IntegradorResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do Integrador não pode estar em branco."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="O email do Integrador não pode estar em branco."
                        )

    def get(self,nome):
        json = ''
        try:
            nome = IntegradorModel.encontrar_pelo_id(nome)
            if nome:
                schema = IntegradorSchema()
                json = schema.dump(nome).data
            else:
                abort(404, message="Integrador {} não está na lista".format(nome))
        except Exception as e:
            print(e)
            abort(404, message="Integrador {} não está na lista".format(nome))

        return json,201


    def post(self):
        json = ''
        try:
            data = IntegradorResource.parser.parse_args()
            print(data)
            nome = data['nome']
            email = data['email']
            integrador = IntegradorModel.encontrar_pelo_nome(nome)
            if integrador :
                return {"message":"Integrador {} já está na lista".format(nome)}
            else:
                integrador = IntegradorModel(nome=nome, email=email)
                integrador.adicionar()
                integrador = IntegradorModel.encontrar_pelo_nome(nome)
                schema = IntegradorSchema()
                json = schema.dump(integrador).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,nome):
        json = []
        try:
            nome = IntegradorModel.encontrar_pelo_id(nome)
            if nome:
                nome.remover()
                lista = IntegradorModel.listar()
                schema = IntegradorSchema(many=True)
                json = schema.dump(lista).data
            else:
                return {"message":"Integrador {} não está na lista".format(nome)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = IntegradorResource.parser.parse_args()
            nome = data['nome']
            email = data['email']

            integrador = IntegradorModel.encontrar_pelo_nome(nome)
            if integrador :
                return {"message":"Integrador {} já está na lista".format(integrador)},200
            else:
                integrador = IntegradorModel(nome=nome, email=email)
                integrador.adicionar()
                schema = IntegradorSchema(many=True)
                integrador = IntegradorModel.encontrar_pelo_nome(nome)
                json = schema.dump(integrador).data
        except Exception as e:
            print(e)
        return json, 201

class IntegradoresResource(Resource):
    def get(self):
        json = []
        try:
            itens = IntegradorModel.listar()
            schema = IntegradorSchema(many=True)
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201