class Conta():
    def __init__(self, numero, cliente, saldo=0, limite=0):
        self.__numero = numero
        self.cliente = cliente
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def saldo_total(self):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __possivel_sacar(self, valor):
        return valor <= self.saldo_total()

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (self.__possivel_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Não há limite para sacar o valor de {}".format(valor))

    def transferir(self, valor, conta_destino, favorecido):
        self.sacar(valor)
        conta_destino.depositar(valor)
        print("Valor de {} transferido para {} com sucesso".format(valor, favorecido.nome))

    def __str__(self):
        return f'Conta numero: {self.numero}, do cliente: {self.cliente}, saldo: {self.saldo}, limite: {self.limite}'

class Conta_Corrente_Pessoa_Fisica(Conta):
    pass

class Conta_Corrente_Pessoa_Juridica(Conta):
    pass
