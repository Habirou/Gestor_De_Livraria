# Desafio Stemis

Bem vindo ao Desafio Stemis!

Este desafio compreende uma das etapas do processo seletivo para a vaga de estagiário em backend.

O desafio consiste na criação de uma API REST usando Python Flask, com simples funções de CRUD, para alguma aplicação interessante e relevante, da sua escolha. Por exemplo, você pode criar um catálogo de produtos, um carrinho de compras, uma gestão de usuários, um sistema de avaliação de serviços (o projeto pode ser algo simples, mas quanto melhor o projeto, mais você se destaca). O importante é que a sua API seja funcional e compreenda as 4 principais operações.

Nunca se esqueça, uma boa API é uma API documentada.

Para conhecer mais sobre a Stemis acesse o nosso [site](https://www.stemis.com.br).

Para ficar informado sobre futuros processos seletivos, siga a gente no Instagram [@stemis.tec](https://www.instagram.com/stemis.tec)



# 1. Ojetivo: 
    #Criar apis para gerenciar os livros de uma livraria
# 2. BaseUrl: 
    #localhost ou Url de prod 
# 3. Endpoints
    # - BaseUrl/Livros (GET) para consultar todos os livros cadastrados
    # - BaseUrl/Livros/id (GET) para consultar um unico livro cadastrado
    # - BaseUrl/Livros (POST) Para cadastrar um livro
    # - BaseUrl/Livros/id (PUT) Para modificar os dados de um livro
    # - BaseUrl/Livros/ (DELETE) Para deletar um livro cadastrado

# 4. Recursos 
    #Livos, Lista de livros

# 5. Passos para executar o projeto apos baixar do github
        - ter python configurado no computador
        - instalar as dependencias do projeto usando pip(flask, flask-pydantic-spec, tinyDB, typing, pydantic ...)
        - para ter os urls de teste local(baseUrl e Url da documentação com swagger), rodar "flask routes"
