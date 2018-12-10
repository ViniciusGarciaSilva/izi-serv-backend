from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.integrador_model import IntegradorModel

class IntegradorSchema(ModelSchema):
    class Meta:
        model = IntegradorModel