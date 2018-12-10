from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.projeto_model import ProjetoModel
from lista.schemas.projeto_schema import ProjetoSchema

class ProjetoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome não pode estar em branco."
                        )
    parser.add_argument('detalhes',
                        type=str,
                        required=True,
                        help="O projeto deve possuir detalhes."
                        )

    def post(self):
        json = ''
        try:
            data = ProjetoResource.parser.parse_args()
            print(data)
            nome = data['nome']
            detalhes = data['detalhes']
            projeto = ProjetoModel.encontrar_pelo_nome(nome)
            if projeto :
                return {"message":"Projeto {} já está na lista".format(nome)}
            else:
                projeto = ProjetoModel(nome=nome, detalhes=detalhes)
                projeto.adicionar()
                projeto = ProjetoModel.encontrar_pelo_nome(nome)
                schema = ProjetoSchema()
                json = schema.dump(projeto).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    def delete(self, projeto):
        json = []
        try:
            projeto = ProjetoModel.encontrar_pelo_id(projeto)
            if projeto:
                projeto.remover()
                lista = ProjetoModel.listar()
                schema = ProjetoSchema(many=True)
                json = schema.dump(lista).data
            else:
                return {"message":"Projeto {} não está na lista".format(projeto)},404
        except Exception as e:
            print(e)
        return json, 201

    def get(self,projeto):
        json = ''
        try:
            projeto = ProjetoModel.encontrar_pelo_nome(projeto)
            if projeto:
                schema = ProjetoSchema()
                json = schema.dump(projeto).data
            else:
                abort(404, message="projeto {} não está na lista".format(projeto))
        except Exception as e:
            print(e)
            abort(404, message="projeto {} não está na lista".format(projeto))

        return json,201

class ProjetosResource(Resource):

    def get(self):
        json = []
        try:
            itens = ProjetoModel.listar()
            schema = ProjetoSchema(many=True)
            json = schema.dump(itens).data
        except Exception as e:
            print(e)
            return {"message": "nao foi possivel obter a lista de projetos."}, 500
        return json,201
    
    
