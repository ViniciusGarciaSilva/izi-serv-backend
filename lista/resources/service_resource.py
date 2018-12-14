from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.service_model import ServiceModel
from lista.schemas.service_schema import ServiceSchema

class ServiceResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="O nome do Service não pode estar em branco."
                        )
    parser.add_argument('details',
                        type=str,
                        required=True,
                        help="O email do Service não pode estar em branco."
                        )
    parser.add_argument('theme',
                        type=str,
                        required=True,
                        help="O email do Service não pode estar em branco."
                        )
    parser.add_argument('funcReq',
                        type=str,
                        required=True,
                        help="O email do Service não pode estar em branco."
                        )
    parser.add_argument('notFuncReq',
                        type=str,
                        required=True,
                        help="O email do Service não pode estar em branco."
                        )
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="O email do Service não pode estar em branco."
                        )

    def get(self,nome):
        json = ''
        try:
            nome = ServiceModel.encontrar_pelo_id(nome)
            if nome:
                schema = ServiceSchema()
                json = schema.dump(nome).data
            else:
                abort(404, message="Service {} não está na lista".format(nome))
        except Exception as e:
            print(e)
            abort(404, message="Service {} não está na lista".format(nome))

        return json,201


    def post(self):
        json = ''
        try:
            data = ServiceResource.parser.parse_args()
            print(data)
            nome = data['name']
            details = data['details']
            theme = data['theme']
            funcReq = data['funcReq']
            notFuncReq = data['notFuncReq']
            status = data['status']
            service = ServiceModel.encontrar_pelo_nome(nome)
            if service :
                return {"message":"Service {} já está na lista".format(nome)}
            else:
                service = ServiceModel(name=nome, details=details, theme=theme, funcReq=funcReq, notFuncReq=notFuncReq, status=status)
                service.adicionar()
                service = ServiceModel.encontrar_pelo_nome(nome)
                schema = ServiceSchema()
                json = schema.dump(service).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self,nome):
        json = []
        try:
            nome = ServiceModel.encontrar_pelo_id(nome)
            if nome:
                nome.remover()
                lista = ServiceModel.listar()
                schema = ServiceSchema(many=True)
                json = schema.dump(lista).data
            else:
                return {"message":"Service {} não está na lista".format(nome)},404
        except Exception as e:
            print(e)
        return json, 201

    def put(self):
        json = ''
        try:
            data = ServiceResource.parser.parse_args()
            print(data)
            nome = data['name']
            details = data['details']
            theme = data['theme']
            funcReq = data['funcReq']
            notFuncReq = data['notFuncReq']
            status = data['status']

            service = ServiceModel.encontrar_pelo_nome(nome)
            if service :
                return {"message":"Service {} já está na lista".format(service)},200
            else:
                service = ServiceModel(name=nome, details=details, theme=theme, funcReq=funcReq, notFuncReq=notFuncReq, status=status)
                service.adicionar()
                schema = ServiceSchema(many=True)
                service = ServiceModel.encontrar_pelo_nome(nome)
                json = schema.dump(service).data
        except Exception as e:
            print(e)
        return json, 201

class ServicesResource(Resource):
    def get(self):
        json = []
        try:
            itens = ServiceModel.listar()
            schema = ServiceSchema(many=True)
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201