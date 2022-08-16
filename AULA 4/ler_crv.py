import csv

ARQUIVO = 'D:\\Curso python\\aula4\\planilha.crv'

with open(ARQUIVO, encoding 'utf-8') as arq:
    tabela = crv.reader(arq)
    for linha in tabela:
        print(linha)
