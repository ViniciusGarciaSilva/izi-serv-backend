from dao import db,Base
from datetime import datetime
class ListaModel(Base):
    __tablename__ = 'listas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey("usuarios.id"))
    usuario = db.relationship("UsuarioModel", back_populates="listas")
    dataCadastro = db.Column(db.DateTime)
    itens = db.relationship("ItemLista", back_populates="lista")

    def __init__(self,nome,usuario_id):
        self.nome = nome
        self.usuario_id = usuario_id
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
