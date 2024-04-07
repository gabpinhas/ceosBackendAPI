# ceosBackendAPI 
## Desafio Backend proposto pela CeosJr - API utilizando DjangoREST

## Introdução
A aplicação consiste em uma API que simula uma Biblioteca Virutal. Sendo possível fazer requisições GET, POST, PUT e DELETE e Acessar uma interface que exibe as informações dos livros.

Utilizei nessa aplicação um ambiente virtual, onde instalei os recursos necessários e dei início ao projeto. Utilizei o Terminal Bash. <br>

## Instruções
Para utilizar a aplicação, você pode executar os seguintes comandos, criando um ambiente virutal, entrando nele e instalando os requirements.

<br>

`python3 -m venv .venv` 

`. .venv/Scripts/activate`

`pip install -r requirements.txt`<br><br>
No terminal, entre no diretório da aplicação e execute `python manage.py runserver` no terminal para iniciar o servidor.

A API agora pode receber suas requisições HTTP, você pode utilizar o Postman para fazê-las.
O endereço padrão seria http://127.0.0.1:8000/library/ , onde são mostrados os livros e suas informações, como 'id', 'title', 'author', 'date', 'genre' e 'publisher'.<br>
Para exibir os dados dos livros no formato JSON http://127.0.0.1:8000/library.json/ <br>
Para exibir os dados de um livro de id = <id> http://127.0.0.1:8000/library/<id>/ <br>
Para exibir os dados de um livro de id = <id> http://127.0.0.1:8000/library/<id>.json/ <br>
Para exibir uma interface contendo informações dos livros em HTML = <id> http://127.0.0.1:8000/booklist/<br>


## Modelo
O modelo Book possui: ['id', 'title', 'author', 'date', 'genre'],<br> sendo id a chave primária, a qual foi automaticamente implementada.


Titulo do Livro <br>
  title : String até 250 caracteres <br> <br>

Autor do Livro <br>
  author : String até 250 caracteres <br> <br>

Data de lançamento do Livro <br>
  date : Campo de Data <br> <br>

Genero do Livro <br>
  genre : String de até 250 caracteres <br> <br>

Editora do Livro <br>
  publisher : String de até 250 caracteres <br> <br>


