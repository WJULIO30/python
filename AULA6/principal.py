

from veiculo import Veiculo,Carro,CarroFalante

def principal():
    veiculo = Veiculo('FIAT', 'Palio', 'AVA-1010', 2010)
    print(veiculo)
    print(veiculo.placa)
    veiculo.ligar()
    veiculo.abastecer()
    veiculo.rodar()


    carro = Carro('VW','Gol', 'BCT-1000', 2015)
    carro.rodar()
    carro.abastecer()
    carro.ligar()
    carro.acelerar()
    print(carro)

    carroFalante = CarroFalante('tesla', 'TST-999999', 'AXY-2221', 2023)
    carroFalante.falar()








if __name__=='__main__':
    principal()
