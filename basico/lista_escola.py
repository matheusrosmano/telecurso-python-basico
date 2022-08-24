from basico.escola import Escola


class ListaEscola:
    def __init__(self):
        self.__escolas = list[Escola]()

    @property
    def escolas(self) -> list[Escola]:
        return self.__escolas

    @escolas.setter
    def escolas(self, escola: Escola) -> None:
        self.__escolas.append(Escola)

    def __len__(self):
        return len(self.escolas)

    def __getitem__(self, item):
        return self.escolas[item]

    def append(self, other: Escola) -> bool:
        for escola in self.escolas:
            if escola.cnpj == other.cnpj:
                return False
        self.__escolas.append(other)
        return True
