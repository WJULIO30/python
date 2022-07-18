
#conta

class Conta:
    
    #contrutor da classe
    def __init__ (self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite



 #sobreescritado método builtin
    def __str__ (self):
        return f'{self.__numero:5} {self.__titular:10} R$ {self.__saldo:5} R$ {self.__limite:5}'

    def deposita (self, valor):
        self.__saldo += valor

    def extrato(self):
        print('-------EXTRATO-------')
        print(f'Titular: {self.__titular}')
        print(f'Numero da conta: {self.__numero}')
        print(f'limite + Saldo: R$ {self.__limite + self.__saldo:.2f}')

        


  #propriedade somente para leitura
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

#método estatico fica armazenado direto na classe, não vai para objeto
    @staticmethod
    def codigo_banco():
        return '001'
    @staticmethod
    def codigos_bancos ():
        return {'BB': '01', 'Caixa': '101', 'Bradesco': '237'}
