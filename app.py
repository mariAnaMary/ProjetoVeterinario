from flask import Flask, render_template, request, redirect
lista = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html',Titulo='Cadastro')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo='Animais cadastrados', lista=lista)

@app.route('/criar',methods=['POST'])
def criar():
    especie = request.form['especie']
    nome = request.form['nome']
    peso = request.form['peso']
    animal = [especie,nome,peso]
    lista.append(animal)
    return redirect('/exibir')


if __name__ == '__main__':
    app.run()
