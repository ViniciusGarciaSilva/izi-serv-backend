from flask import Flask
from flask_cors import CORS
from flask_restful import Api
#Importar cada recurso usado pela API.
from lista.resources.item_resource import ItemResource, ItensResource
from lista.resources.usuario_resource import UsuarioResource,UsuariosResource
from lista.resources.lista_resource import ListaResource, ListasResource
from lista.resources.projeto_resource import ProjetosResource, ProjetoResource
from lista.resources.cliente_resource import ClientesResource, ClienteResource
from lista.resources.integrador_resource import IntegradoresResource, IntegradorResource
from lista.resources.prestador_resource import PrestadoresResource, PrestadorResource
from lista.resources.service_resource import ServicesResource, ServiceResource

app = Flask(__name__)
#Configurações relativas ao sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = b'\xc4]gW\x0f\x8d\xc8\x05ocG\xf1\xb1j,{'

#fim configurações relativas ao sqlalchemy
api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}}) #O uso do cors
#cria as tabelas do banco de dados, caso elas não estejam criadas
@app.before_first_request
def create_tables():
    print("criar tabelas")
    db.create_all()
#fim criaçaõ de tabelas

api.add_resource(ItensResource, '/itens')
api.add_resource(ItemResource, '/item', '/item/<string:item>')
api.add_resource(ProjetosResource, '/projetos')
api.add_resource(ProjetoResource, '/projeto', '/projeto/<string:projeto>')
api.add_resource(ClienteResource, '/cliente', '/cliente/<string:nome>')
api.add_resource(ClientesResource, '/clientes')
api.add_resource(IntegradorResource, '/integrador', '/integrador/<string:nome>')
api.add_resource(IntegradoresResource, '/integradores')
api.add_resource(PrestadorResource, '/prestador', '/prestador/<string:nome>')
api.add_resource(PrestadoresResource, '/prestadores')
api.add_resource(ServicesResource, '/services')
api.add_resource(ServiceResource, '/service')

api.add_resource(ListasResource, '/listas')
api.add_resource(ListaResource, '/lista','/lista/<string:lista>')
api.add_resource(UsuarioResource,'/usuario','/usuario/<string:nome>')
api.add_resource(UsuariosResource, '/usuarios')

if __name__ == '__main__':
    from dao import db
    db.init_app(app)
    app.run(host="0.0.0.0", port=80)
