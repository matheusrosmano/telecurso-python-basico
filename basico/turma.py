from aluno import Aluno
from escola import Escola


class Turma:
    def __init__(self):
        self.__horario = None
        self.__alunos = []
        self.__escola = Escola()

    @property
    def escola(self) -> Escola:
        return self.__escola

    @escola.setter
    def escola(self, escola: Escola) -> None:
        self.__escola = escola

    @property
    def alunos(self) -> list[Aluno]:
        return self.__alunos

    @alunos.setter
    def alunos(self, aluno: Aluno) -> None:
        self.__alunos.append(aluno)
