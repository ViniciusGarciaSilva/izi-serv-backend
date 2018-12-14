from dao import db,Base
from datetime import datetime

class ServiceModel(Base):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    details = db.Column(db.String(200))
    theme = db.Column(db.String(200))
    funcReq = db.Column(db.String(200))
    notFuncReq = db.Column(db.String(200))
    status = db.Column(db.String(200))
    
    def __init__(self, name, details, theme, funcReq, notFuncReq, status):
        self.name = name
        self.details = details
        self.theme = theme
        self.funcReq = funcReq
        self.notFuncReq = notFuncReq
        self.status = status


    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(name=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()