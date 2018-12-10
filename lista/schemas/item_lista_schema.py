from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.item_lista_model import ItemLista
class ItemListaSchema(ModelSchema):
    item = fields.Nested("ItemSchema", many=False, only=['nome'])
    #preco = fields.Str()
    class Meta:
        model: ItemLista