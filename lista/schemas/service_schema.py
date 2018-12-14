from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.service_model import ServiceModel

class ServiceSchema(ModelSchema):
    class Meta:
        model = ServiceModel