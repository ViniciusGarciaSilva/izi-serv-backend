from dao import db,Base

class ItemLista(Base):
    __tablename__ = 'itenslistas'
    lista_id = db.Column(db.Integer, db.ForeignKey('listas.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('itens.id'), primary_key=True)
    preco = db.Column(db.String(100))
    item = db.relationship("ItemModel", back_populates="listas", uselist=False)
    lista = db.relationship("ListaModel", back_populates="itens", uselist = False)
    def __init__(self, preco):
        self.preco = preco