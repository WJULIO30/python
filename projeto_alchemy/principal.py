
from models import Produto
from config import db

#apaga todas as tabelas
db.drop_all()

#cria todas as tabelas do banco de dados
db.create_all()

#cria uma entidade
tv = Produto(descricao='TV SAMSUNG', preco=1999.9, quantidade=10)

#ainda sem id
print(tv)

#salva no banco
db.session.add(tv)   #insert into Produto values.....
db.session.commit()
#agora com id
print(tv)

#alterando a descrição

tv.descricao = 'TV LG 50'
db.session.add(tv)
db.session.commit()

#cria outra entidade

fogao = Produto(descricao='Fogão 6 bocas', preco=2500, quantidade=5)

#salva
db.session.add(fogao)
db.session.commit()

#consulta todos os produtos cadastrados (SELECT  * FROM produto)
produtos = Produto.query.all()
for p in produtos:
    print(p)

#buscando um unico item
porId = Produto.query.filter_by(id=1).first()
print('busca por id: ', porId)


porDescricao= Produto.query.filter_by(descricao='TV LG 50').all()
print('buscar por descricão:' , porDescricao)

#apaga
produto= Produto.query.filter_by(id=2).first()
if produto:
    db.session.delete(produto)
    db.session.commit()
    print('apagou')
else :
    print('não apagou')