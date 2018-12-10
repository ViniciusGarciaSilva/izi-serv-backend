from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.projeto_model import ProjetoModel

class ProjetoSchema(ModelSchema):
    class Meta:
        model = ProjetoModel