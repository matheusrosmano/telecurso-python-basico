from usuario import Usuario
from validators import cpf_is_valid


class Aluno(Usuario):
    def __init__(self):
        super().__init__()

    def cadastrar_matricula(self, matricula: str) -> None:
        self._matricula = matricula

    def cadastrar_documento(self, documento: str) -> None:
        documento = str(documento)
        documento = documento.strip()
        if not cpf_is_valid(documento):
            raise ValueError("cpf isn't valid")
        self._documento = documento
