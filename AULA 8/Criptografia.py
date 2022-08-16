#Criptografia

frase = input('Digite uma frase:')

for letra in frase:

    #converte a letra inteiro
    inteiro = ord(letra)

    #converte inteiro em binario
    binario = format(inteiro, 'b')

    # rola para esquerda
    binario = binario[1:7] + binario[0]

    #converte binario em inteiro
    inteiro = int(binario, 2)

    print (chr (inteiro), end='')

