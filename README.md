# lista-de-compras-backend
Backend do Projeto Lista de Compras para a disciplina PCS3643 - 2018

Clonar o projeto através da linha de comando

Entrar no diretório do Projeto

Criar um ambiente virtual de python para o projeto 
pip install virtualenv

virtualenv --version

virtualenv venv

Abrir o editor vscode

Escolher o interprete do Python que está no venv

Abrir um terminal do vscode
Verificar que o ambiente virtual venv está selecionado, se não, selecionar ele.

Instalar as dependências via 
pip3 install -r requirements.txt

Executar o projeto via 
python app.py

Abrir o Postman
Criar requisições para teste da API

POST
url: http://127.0.0.1:5000/item

Headers
key:Content-Type
value:application/json
Body
raw
{"item":"abobora"}

GET
url: http://127.0.0.1:5000/item/abobora

PUT
url: http://127.0.0.1:5000/item

Headers
key:Content-Type 
value:application/json
Body
raw
{"item":"tomates"}

GET
url: http://127.0.0.1:5000/itens

DELETE
url: http://127.0.0.1:5000/item/abobora

