import uuid
from abc import ABC, abstractmethod
from datetime import datetime

from validators import username_is_valid, email_is_valid


class Usuario(ABC):
    def __init__(self) -> None:
        self.__id = uuid.uuid4()
        self.__username = None
        self.__nome = None
        self.__email = None
        self._matricula = None
        self.__data_cadastro = datetime.now()
        self.__documento = None

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @id.setter
    def id(self, id_usuario: str) -> None:
        self.__id = uuid.UUID(id_usuario)

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str) -> None:
        username = username.strip()
        if not username_is_valid(username):
            raise ValueError("Username isn't valid")
        self.__username = username

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        email = email.strip()
        if not email_is_valid(email):
            raise ValueError("Email isn't valid")
        self.__email = email

    @property
    def matricula(self) -> str:
        return self._matricula

    @abstractmethod
    def cadastrar_matricula(self, matricula: str) -> None:
        pass

    @property
    def documento(self) -> str:
        return self.documento

    @abstractmethod
    def cadastrar_documento(self, documento: str) -> None:
        pass

    def __eq__(self, other) -> bool:
        return self.id == other.id
