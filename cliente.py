class Cliente:

    def __init__(self, nome, sobrenome, numero):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__numero = numero

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f'Nome: {self.__nome} {self.__sobrenome}, Numero do cliente: {self.__numero}'
