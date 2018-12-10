from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.lista_model import ListaModel
from lista.schemas.usuario_schema import UsuarioSchema
from lista.schemas.item_lista_schema import ItemListaSchema

class ListaSchema(ModelSchema):
    itens = fields.Nested('ItemListaSchema', many=True)
    usuario = fields.Nested('UsuarioSchema', many=False, only=['nome'])
    class Meta:
        model = ListaModel