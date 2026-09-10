from flask import Flask, render_template, request, redirect, url_for, session, blueprint
import models
from blueprints.auth import auth_bp
from blueprints.catalog import catalog_bp

app = Flask(__name__)
app.secret_key = "chave-secreta"

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)

@app.route("/livro/<int:livro_id>/resenhar", methods=["POST"])
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    if models.buscar_livro(livro_id):
        models.resenhas.append({
            "id": models.proximo_id_resenha,
            "livro_id": livro_id,
            "usuario": session["usuario"],
            "texto": request.form["texto"],
            "nota": int(request.form["nota"]),
        })
        models.proximo_id_resenha += 1
    return redirect(url_for("ver_livro", livro_id=livro_id))


if __name__ == "__main__":
    app.run(debug=True)
