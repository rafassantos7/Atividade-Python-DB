from models.usuario import Usuario
from sqlalchemy import Session


class UsuarioRepository:
    def __init__(self, session=Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):

        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisar_usuario(self, id: int):
        return self.session.query(Usuario).filter_by(id=id).first()

    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def listar_usuarios(self):
        self.session.query(Usuario).all()
