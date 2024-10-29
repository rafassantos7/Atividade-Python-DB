from repositories.usuario_repositories import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:
    def __init__(self,repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome : str, email: str, senha: str):

        try:
            usuario = Usuario(nome = nome, email = email, senha = senha)
            cadastrado = self.repository.pesquisar_usuario(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
        except TypeError as erro:
            print(f"Erro ao salvar usuario: {erro} ")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_usuario(self):
        self.repository.listar_usuarios()