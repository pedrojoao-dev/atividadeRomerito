from flask import Flask, render_template, redirect, session, url_for
import models 

app = Flask(__name__)

app.secret_key = "bomDia"

@app.route("/")
def index():
    
    return render_template('index.html', livro = models.buscar_livros(None))

@app.route("/livro/<int:livro_id>")
def livro(livro_id):
    livro_buscar = models.resenhas_do_livro(livro_id)
    if "usuario" in session:
        if not livro_buscar:
            return ("id não existe", 404)
        elif livro_buscar:

            return render_template ('livro.html', buscar_resenha = models.resenhas_do_livro(livro_id))

    return redirect(url_for('login'))

@app.route("/login", method = ['GET', 'POST'])
def login():
    pass


