from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.prestador_model import PrestadorModel

class PrestadorSchema(ModelSchema):
    class Meta:
        model = PrestadorModel