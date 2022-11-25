# Kontent

**Resumo:**

A aplicação é um CRUD aonde o conceito é criar turmas de um curso aonde serão passados o número de vagas pro curso, nome do curso, descrição do curso e o nome da turma.

**Tecnologias utilizadas:**

Python | Django | Django Rest Framework | Sqlite3

Para clonar o arquivo em sua máquina use o seguinte comando no seu terminal:

````
git clone git@github.com:anjosdelacerda/kontent.git
````

Para que a aplicação funcione será necessário instalar o Python em sua máquina, você encontrará informações de como fazer isso na <a href="https://docs.python.org/3/tutorial/">documentação</a>. 

O pip também será necessário para o gerenciamento de instalações de dependências, na <a href="https://pip.pypa.io/en/stable/getting-started/"> documentação </a> você terá um passo-a-passo de como instala-lo. 

No terminal dentro da sua pasta clonada crie uma variável de abiente com este comando:

````
python -m venv venv
````

Agora ative este variável para que você possa instalas as dependências da aplicação com segurança:

````
source venv/bin/activate
````

Agora instale todas as dependências rodando este comando no terminal da pasta clonada:

````
pip install -r requirements.txt
````

Dentro da aplicação haverá um arquivo chamado **workspace.json** aonde vocẽ poderá importa-lo em seu testador de rotas favorito, os dados serão persistidos no arquivo **db.sqlite4**.
