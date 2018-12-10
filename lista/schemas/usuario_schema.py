from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.usuario_model import UsuarioModel
class UsuarioSchema(ModelSchema):
    listas = fields.Nested('ListaSchema',many=True, only=['nome'])
    class Meta:
        model = UsuarioModel