
# Url da documentacao: https://livraria-cxub.onrender.com/doc/swagger#/default/obterLivros
# Base Url: https://livraria-cxub.onrender.com
# Consulte primeiro o arquivo README.md para entender mais o projeto

from typing import Optional
from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query


#Servidor
app = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Apis da Livraria", version="v1.0", path="doc")
#Documentacao
spec.register(app)  

#Banco de dados
database = TinyDB('database.json') 

#Modelo dum Livro
class Livro(BaseModel):
    id: Optional[int] 
    titulo: str
    autor: str

#Modelo duma Lista Livro
class ListaDeLivros(BaseModel):
    livros: list[Livro]
    count: int

# Consultar os livros cadastrados
@app.route('/livros', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=ListaDeLivros, HTTP_403=None), tags=['api'])
def obter_livros():
    """Consultar todos os livros cadastrados no Banco de dados."""
    # return jsonify(livros)
    todos_livros = database.all()
    return jsonify(
        ListaDeLivros(
            livros=todos_livros,
            count=len(todos_livros)
        ).dict()
    )


# Consultar um livro cadastrado
@app.route('/livros/<int:id>', methods=['GET'])
@spec.validate(resp=Response(HTTP_200=Livro), tags=['api'])
def obter_livro_por_id(id):
    """Consultar um livro no Banco de dados pelo id."""
    livro = database.search(Query().id == id)
    if not livro:
        return {'message': 'Esse Livro não existe'}, 404
    return jsonify(livro[0])
    


# Editar os dados de um livro cadastrado
@app.route('/livros/<int:id>', methods=['PUT'])
@spec.validate(body=Request(Livro), resp=Response(HTTP_200=Livro, HTTP_403=None), tags=['api'])
def editar_livro_por_id(id):
    """Editar os dados de um livro no Banco de dados."""
    livro_alterado = request.get_json()
    if not database.contains(Query().id == id):
        return {'message': 'Livro não encontrado'}, 404
    if database.contains(Query().titulo == livro_alterado['titulo']):
        return {'message': 'Um Livro com esse titulo já existe'}, 409
    livro_alterado.pop('id', None)
    database.update(livro_alterado, Query().id == id)
    return jsonify(livro_alterado)


# Cadastrar um livro
@app.route('/livros', methods=['POST'])
@spec.validate(body=Request(Livro), resp=Response(HTTP_200=Livro), tags=['api'])
def cadastrar_livro():
    """Insere um livro no Banco de dados."""
    novo_Livro = request.get_json()
    if database.contains(Query().titulo == novo_Livro['titulo']):
        return {'message': 'Livro já existe'}, 409
    
    # Gere um ID automaticamente
    max_id = max([book['id'] for book in database.all()], default=0)
    novo_Livro['id'] = max_id + 1

    database.insert(novo_Livro)
    return jsonify(novo_Livro)


# Excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
@spec.validate(resp=Response(HTTP_200=None, HTTP_403=None), tags=['api'])
def excluir_livro(id):
    """Excluir um livro no Banco de dados."""
    if not database.contains(Query().id == id):
        return {'message': 'Livro não encontrado'}, 404
    database.remove(Query().id == id)
    return {'message': 'Livro excluído com sucesso'}


if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)