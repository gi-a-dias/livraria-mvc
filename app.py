# app.py (Controller)
from flask import Flask, render_template, request
from livraria import filtrar_por_genero

app = Flask(__name__)


@app.route('/')
def index():
    # Pega o parâmetro de filtro da URL (ex: /?genero=Fantasia)
    genero_selecionado = request.args.get('genero')

    # Chama o Model para obter os dados processados
    livros = filtrar_por_genero(genero_selecionado)

    # Retorna a View renderizada passando os dados
    return render_template('index.html', livros=livros, genero=genero_selecionado)


if __name__ == '__main__':
    app.run(debug=True)