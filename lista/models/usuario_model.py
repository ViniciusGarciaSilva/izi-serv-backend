
from dao import db,Base
from datetime import datetime

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200),unique=True)
    email = db.Column(db.String(200),unique=True)
    dataCadastro = db.Column(db.DateTime)
    listas = db.relationship("ListaModel",back_populates="usuario")

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.dataCadastro = datetime.now()

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
