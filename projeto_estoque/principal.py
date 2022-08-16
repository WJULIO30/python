from dao import ProdutoDao
from produto import Produto
from flask import Flask, render_template, request, redirect, url_for, flash, session

dao = ProdutoDao('banco.db')
produto = Produto('Computador', 4555, 10, 1)


app = Flask(__name__)
app.secret_key = "wjo"

@app.route('/')
def inicio():
    lista = dao.listar()
    return render_template('relatorio.html', titulo='Relatório de estoque', produtos=lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html', titulo='Cadastra Novo Produto')

@app.route('/salvar', methods=['POST'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto = Produto(descricao, preco, quantidade, id)
    dao.salvar(produto)

    return redirect(url_for('inicio'))

@app.route('/deletar/<string:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    dao.deletar(id)
    flash('O Produto foi removido com sucesso!')
    return redirect(url_for('inicio'))

@app.route('/editar/<string:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produto = dao.buscar_por_id(id)
    return render_template('editar.html', titulo='editar Produto', produto=produto)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods= ['POST'])
def autenticar():
    if request.form['senha'] == '123':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect(url_for('inicio'))
    else:
        flash('Senha invalida! Tente novamente')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)



