
#PRODUTO.PY
#CLASSE Produto
class Produto:
    
    #construtor da classe
    def __init__(self, nome, descricao, valor, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

    #função builtin
    def __str__ (self):
        return f'None: {self.nome:10} \t Desc: {self.descricao:10} \tR$  {self.valor} \tQuant: {self.quantidade}'



