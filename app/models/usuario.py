from sqlalchemy import Colunm, String, Integer
from sqlalchemy.orm import declarative_base as Base
from config.database import db


class Usuario(Base):
    
    __tablename__ = "usuarios"

    id = Colunm(Integer, autoincrement = True, primary_key = True)
    nome = Colunm(String(150))
    email = Colunm(String(150))
    senha = Colunm(String(150))

    def __init__(self,nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=db)