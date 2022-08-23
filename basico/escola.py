from validators import cnpj_is_valid


class Escola:
    def __init__(self):
        self.__nome = None
        self.__endereco = None
        self.__cnpj = None

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        self.__endereco = endereco

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str) -> None:
        cnpj = str(cnpj)
        cnpj = cnpj.strip()

        if not cnpj_is_valid(cnpj):
            raise ValueError("Cnpj isn't valid")
        self.__cnpj = cnpj

    def __str__(self):
        texto = f"<< CNPJ: {self.cnpj} | Nome: {self.nome} >>"
        return texto
