'''
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))
'''
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo uma conta {}.".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo de {} é de R$ {}.".format(self.titular,self.saldo))

    def __pode_sacar(self, valor_sacar):
        valor_disponivel = self.__limite + self.saldo
        return valor_sacar <= valor_disponivel

    def sacar(self, valor):
        '''
        x = float(input("Quanto deseja sacar? "))
        self.saldo -= x
        '''
        if (self.pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor de {} a ser sacado excedeu o limite.".format(valor))

    def depositar(self, valor):
        '''
        y = float(input("Quanto deseja depositar? "))
        self.saldo += y
        '''
        self.saldo += valor

    def transferir(self, valor, final):
        self.sacar(valor)
        final.depositar(valor)

    @staticmethod
    def condigo_banco():
        return "001"

    @staticmethod
    def condigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
