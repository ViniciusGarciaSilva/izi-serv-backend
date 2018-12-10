from dao import db,Base
from datetime import datetime

class ItemModel(Base):
    __tablename__ = 'itens'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True)
    data_criacao = db.Column(db.DateTime)
    listas = db.relationship("ItemLista", back_populates="item")

    def __init__(self, nome):
        self.nome = nome
        self.data_criacao = datetime.now()

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()