from usuario import Usuario


class Aluno(Usuario):
    def __init__(self):
        super().__init__()

    def cadastrar_matricula(self, matricula: str) -> None:
        self._matricula = matricula
