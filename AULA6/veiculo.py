import win32com.client as win32

class Veiculo:

    #Contrutor da classe
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


    #sobrescreve a função builtin padrão
    def __str__(self):
        return f'Veiculo {self.marca} Modelo: {self.modelo} Placa:{self.placa} Ano:{self.ano}'

    def ligar(self):
        print('Veiculo ligado...')

    def rodar(self):
        print('Veiculo rodando...')

    def abastecer(self):
        print('veiculo abastecendo...')






class Carro(Veiculo):

    def __int__(self, marca, modelo, placa, ano):
        #chama o contrutor da superclasse (classe mae)
        super().__init__(marca, modelo, placa,ano)


    #sobrescrita do metodo
    def ligar(self):
        print('carro ligado')

    def acelerar(self):
        print('carro acelerando... VRUMMMM')

class CarroFalante(Carro):
    def __int__(self, marca, modelo, placa, ano):
        #chama o contrutor da superclasse (classe mae)
        super().__init__(marca, modelo, placa,ano)

    def falar(self):
        speaker = win32.Dispatch('SAPI.SpVoice')
        speaker.Speak('Carro dirigindo sozinho')