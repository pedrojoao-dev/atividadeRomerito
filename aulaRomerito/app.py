from flask import Flask, render_template, redirect, session, url_for
import models 

app = Flask(__name__)

app.secret_key = "bomDia"

@app.route("/")
def index():
    
    return render_template('index.html', livro = models.buscar_livros(None))