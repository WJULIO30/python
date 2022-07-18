#test_conta

from conta import Conta

if __name__== '__main__':
    contaJoao = Conta(123, 'João da Silva', 200, 1000)
    print(contaJoao)
    contaJoao.deposita(100)
    print(contaJoao.saldo)

    contaJoao.limite = 5000
    print(contaJoao.limite)
    contaJoao.extrato()
#função estatica = chama direto na classe
    print(Conta.codigo_banco())

    codigos = Conta.codigos_bancos()
    print('\nCódigos de todos os bancos:')
    print('Banco do Brasil: ', codigos['BB'])
    print('Caixa:', codigos['Caixa'])
    print('Bradesco:', codigos['Bradesco'])      
          
