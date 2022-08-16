# Framework ORM-SQLALCHEMY

# site oficial
# https://flask-sqlalchemy.palletsprojects.com

# No terminal do pycharmy digita :
# pip install Flask Flask-SQLALchemy

#caso ocorra erro de segurança no terminal do pycharm, é necessario
#mudar a politica de segurança do powershell
#A. Executar Power shell no modo administardor
#b Set-ExecutionPolicy remoteSigned
#c A (all)


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurando o acesso ao banco de dados do SQLAlquemy
#basedir = 'D:\cursor Python\projeto_Alquemy'
basedir = os.path.abspath(os.path.dirname(__file__))

uri = 'sqlite:///' + os.path.join(basedir, 'database.db')
#para Mysql
#mysql://usarname:passaword@host:port/database_name
#exemplo: 'mysql://root:senha@localhost:3306/nome_banco'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#cria o banco de dados do app
db = SQLAlchemy(app)






