from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.cliente_model import ClienteModel

class ClienteSchema(ModelSchema):
    class Meta:
        model = ClienteModel