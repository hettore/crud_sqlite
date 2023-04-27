from flask import Flask, render_template, request, redirect, url_for
import repositorio
import os

caminho = f"{os.path.dirname(__file__)}\\db\\produtos.db"

app = Flask(__name__)

#LEMBRE-SE -> 
# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#É preciso criar rotas que levem em conta as seguintes funcionalidades:
#Listar todos os produtosn o template index.html
@app.route("/")
def listagem_produtos():
    return render_template('index.html', produtos=repositorio.retornar_produtos())


#Abrir um produto específico (carregando seus dados) no template cadastro.html
@app.route("/produto/<int:id>", methods=["GET"])
def exibir_produto(id):
    
    id, nome, descricao, preco, imagem = repositorio.retornar_produto(id)
    return render_template('cadastro.html', id=id, nome=nome, descricao=descricao, preco=preco, imagem=imagem)
    

#Abrir o template cadastro.html apenas com o id preenchido para permitir novo cadastro
#Dar função aos botões excluir e salvar no template cadastro.html
@app.route("/produto/<int:id>", methods=["POST"])
#a linha acima indica que a mesma rota que já havíamos criado antes foi reacriada
# #com o método POST, ou seja, quando o usuário enviar dados    
def editar_produto(id):
    if "excluir" in request.form:
        #Aqui estamos verificando que "excluir" está contido na requisição, ou seja
        #o usuário clicou no botão excluir do formulário
        repositorio.remover_produto(id)
    elif "salvar" in request.form:
        #Aqui estamos verificando que "salvar" está contido na requisição, ou seja,
        #o usuário clicou em "salvar"
        produto = {} #Criando um dicionário vazio para conter os dados do produto que será salvo
        produto["nome"] = request.form["nome"] #colocamos no dicionário o conteúdo que veio do formulário
        produto["descricao"] = request.form["descricao"]
        produto["preco"] = request.form["preco"]
        produto["imagem"] = request.form["imagem"]

        #preciso definir se vou SALVAR um novo produto ou ATUALIZAR um produto já existente
        produto_existente = repositorio.retornar_produto(id)
        #vamos testar se o id do produto está no dicionário que contém todos eles.
        if produto_existente[1]: # caso a tupla q voltou do banco de dados tenha dados na coluna 1, vamos atualizar o produto. Caso contrario, vamos criar um novo
            produto["id"] = id
            repositorio.atualizar_produto(**produto) #caso o id já exista, vamos chamar a função atualizar_produto, indicando o id e os novos dados
        else:
            repositorio.criar_produto(**produto) #caso a id não exista, vamos chamar a função criar_produto passando os dados do dicionário
            #repositorio.criar_produto(nome=produto['nome'], descricao=produto['descricao'], preco=produto['preco'], imagem=produto['imagem'])
    #o nosso return está fora dos ifs porque será executado INDEPENDENTEMENTE do botão que for clicado
    return redirect(url_for('listagem_produtos'))



app.run(debug=True)