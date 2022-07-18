

from produto import Produto


#ler_csv.py


import csv

ARQUIVO = 'E:\\Curso python WELLINGTON\\aula 5\\planilha.csv'
primeira = True
lista_produtos = []

with open(ARQUIVO, encoding='utf-8') as arq:
    tabela = csv.reader(arq)
    for linha in tabela:
        if primeira:
            primeira = False
            continue
        lista = linha[0].split(';')
        nome = lista[0]
        desc = lista [1]
        valor = lista[2]
        quant = lista[3]
        p = Produto(nome, desc, valor, quant)
        lista_produtos.append(p)



for item in lista_produtos:
   print(item)
        
