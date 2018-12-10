from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.schemas.lista_schema import ListaSchema
from lista.models.item_model import ItemModel

class ItemSchema(ModelSchema):
    listas = fields.Nested("ListaSchema",many=True, exclude=('itens','usuario'))
    class Meta:
        model = ItemModel