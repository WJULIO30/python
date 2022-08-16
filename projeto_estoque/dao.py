#DAO = DATA ACESS OBJECT = Objeto de Acesso a dados
#Onde você increve os comandos SQL
#INTALAR SQLSTUDIO = HTTPS://sqlitestudio.pl
import sqlite3

#Comandos SQL
from produto import Produto

SQL_PREPARA_BANCO = 'create table if not exists produto ' \
                    '(descricao varchar(60) not null, ' \
                    'preco double not null, ' \
                    'quantidade integer not null)'

SQL_SALVA_PRODUTO = 'insert into produto values (?,?,?)'
SQL_LISTA_PRODUTO = 'select descricao, preco, quantidade, rowid from produto'
SQL_LISTA_PRODUTO_POR_ID = 'select descricao, preco, quantidade, rowid from produto where rowid=?'
SQL_ATUALIZA_PRODUTO = 'update produto set descricao=?, preco=?, quantidade=? where rowid=?'
SQL_DELETA_PRODUTO = 'delete from produto where rowid=?'

class ProdutoDao:

    #construtor da classe
    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.prepara_banco()

    def prepara_banco(self):
        print('conectando banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        conexao.cursor().execute(SQL_PREPARA_BANCO)
        #COMITANDO SENÃO NADA EFEITO
        conexao.commit()
        print('ok')
    def salvar(self, produto):
        print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()

        #
        if (produto.id != None and len(produto.id) > 0):
            cursor.execute(SQL_ATUALIZA_PRODUTO, (produto.descricao,
                                           produto.preco,
                                           produto.quantidade,produto.id))

        else:
            cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao,
                                           produto.preco,
                                           produto.quantidade))
            produto.id= cursor.lastrowid

        conexao.commit()
        print('ok')
        return produto

    def buscar_por_id(self, id):
        #criar conexão com banco de dados
        conexao = sqlite3.connect(self.__nome_banco)
        #obtem o cursor do banco
        cursor = conexao.cursor()
        #executa o comando SQL
        cursor .execute(SQL_LISTA_PRODUTO_POR_ID,  [str(id)])
        #recupera a consulta em forma de tupla
        tupla = cursor.fetchone()
        #cria um objeto produto a partir da tupla e retorna este
        return Produto(tupla[0], tupla[1], tupla[2], tupla[3])

    def deletar(self,id):
        conexao = sqlite3.connect(self.__nome_banco)
        conexao.cursor().execute(SQL_DELETA_PRODUTO, [str(id)])
        conexao.commit()

    #lista todos itens da tabela
    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_LISTA_PRODUTO)
        lista = cursor.fetchall()
        produtos = []
        for tupla in lista:
            produto = Produto(tupla[0], tupla[1], tupla[2], tupla[3])
            produtos.append(produto)
        return  produtos

