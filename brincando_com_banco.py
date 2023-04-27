import sqlite3
import os

caminho = f"{os.path.dirname(__file__)}\\db\\produtos.db"

## ESTE ARQUIVO CONTÉM O USO DAS PRINCIPAIS OPERAÇÕES DE BANCOS DE DADOS. CADA REMOVA OS COMENTÁRIOS (# ) DO INÍCIO DE CADA LINHA DE COMANDOS PARA FAZER OS RESPECTIVOS TESTES.
## DICA: O VSCode conta com a opção "Toggle Line Comment" que automaticamente inclui ou exclui comentários do início das linhas selecionadas.



## PARA EXECUTAR UM SELECT (OPERAÇÃO QUE RETORNA DADOS DO BANCO) SEM UMA CLÁUSULA DE RESTRIÇÃO (WHERE) DEVEMOS USAR O MÉTODO FETCHALL() DO CURSOR, POIS ESPERA-SE RECEBER VÁRIAS LINHAS COMO RESULTADO
# conn = sqlite3.connect(caminho) #iniciando a conexão com o arquivo de banco de dados SQLite
# cursor = conn.cursor() #criando um novo cursor para poder realizar operações neste banco
# sql_select = "SELECT * FROM produtos" #uma variável string apenas para escrevermos o comando que será executado. É opcional, mas ajuda na legibilidade
# cursor.execute(sql_select) #execução do comando sql que está escrito na variável sql_select
# produtos = cursor.fetchall() #retorno de TODAS as linhas que foram obtidas após a execução do comando
# print("---- EXECUÇÃO DE SELECT SEM WHERE NA TABELA PRODUTOS ----")
# print(f"O tipo do objeto produtos é {type(produtos)}")
# print(f"Seu conteúdo é {produtos}")
# print()
# conn.close()#fechando a conexão com o banco de dados. É MUITO importante não esquecer de fechar a conexão com o banco para evitar erros

# # PARA EXECUTAR UM SELECT (OPERAÇÃO QUE RETORNA DADOS DO BANCO) COM UMA CLÁUSULA DE RESTRIÇÃO (WHERE) DEVEMOS USAR O MÉTODO FETCHONE() DO CURSOR, POIS ESPERA-SE RECEBER APENAS UMA LINHA COMO RESULTADO
# conn = sqlite3.connect(caminho) #iniciando a conexão com o arquivo de banco de dados SQLite
# cursor = conn.cursor() #criando um novo cursor para poder realizar operações neste banco
# sql_select = "SELECT * FROM produtos WHERE id_produto=?" #uma variável string apenas para escrevermos o comando que será executado. É opcional, mas ajuda na legibilidade. 
# cursor.execute(sql_select, (1, )) #execução do comando sql que está escrito na variável sql_select. Como passamos um ? para indicar a inclusão de um argumento, precisamos passar os valores em forma de tupla.
# produto = cursor.fetchone() #retorno da única linha que foi obtida após a execução do comando
# print("---- EXECUÇÃO DE SELECT SEM WHERE NA TABELA PRODUTOS ----")
# print(f"O tipo do objeto produto é {type(produto)}")
# print(f"Seu conteúdo é {produto}")
# print()
# conn.close()#fechando a conexão com o banco de dados. É MUITO importante não esquecer de fechar a conexão com o banco para evitar erros

# # PARA EXECUTAR UM INSERT (OPERAÇÃO QUE INCLUI DADOS NO BANCO), PRECISAMOS UTILIZAR O MÉTODO COMMIT, QUE GRAVA NO BANCO AS ALTERAÇÕES QUE FOREM FEITAS
# conn = sqlite3.connect(caminho) #iniciando a conexão com o arquivo de banco de dados SQLite
# cursor = conn.cursor() #criando um novo cursor para poder realizar operações neste banco
# sql_insert = "INSERT INTO produtos (nome_produto, descricao_produto, preco_produto, imagem_produto) VALUES (?, ?, ?, ?)"
# cursor.execute(sql_insert, ("Placa RTX3080", "PLACA DE VÍDEO RTX3080 - 12GB DE RAM", 4500.00, "3080.jpg")) #execução do comando sql que está escrito na variável sql_insert. Como passamos um ? para indicar a inclusão de um argumento, precisamos passar os valores em forma de tupla.
# id = cursor.lastrowid #recuperação do último id que foi gerado nesta tabela por este cursor, portanto, do id do produto que acabamos de inserir
# conn.commit() #salvando as alterações no banco de dados
# conn.close() #fechando a conexão com o banco de dados. É MUITO importante não esquecer de fechar a conexão com o banco para evitar erros
# print("Inclusão de dados bem sucedida!")
# print()



# # PARA EXECUTAR UM UPDATE (OPERAÇÃO QUE ATUALIZA DADOS DO BANCO), PRECISAMOS UTILIZAR O MÉTODO COMMIT, QUE GRAVA NO BANCO AS ALTERAÇÕES QUE FOREM FEITAS
# conn = sqlite3.connect(caminho) #iniciando a conexão com o arquivo de banco de dados SQLite
# cursor = conn.cursor()#criando um novo cursor para poder realizar operações neste banco
# sql_update = "UPDATE produtos SET nome_produto=?, descricao_produto=?, preco_produto=?, imagem_produto=? WHERE id_produto = ?"
# cursor.execute(sql_update, ("Ipad Pro", "Ipad 11 PRO, 128gb, Cinza", 1500.00, "ipad_pro.jpg", 1))  #execução do comando sql que está escrito na variável sql_insert. Como passamos um ? para indicar a inclusão de um argumento, precisamos passar os valores em forma de tupla.
# conn.commit()#salvando as alterações no banco de dados
# conn.close()#fechando a conexão com o banco de dados. É MUITO importante não esquecer de fechar a conexão com o banco para evitar erros
# print("Alteração de dados bem sucedida!")
# print()


# PARA EXECUTAR UM DELETE (OPERAÇÃO QUE REMOVE DADOS DO BANCO), PRECISAMOS UTILIZAR O MÉTODO COMMIT, QUE GRAVA NO BANCO AS ALTERAÇÕES QUE FOREM FEITAS
conn = sqlite3.connect(caminho)
cursor = conn.cursor()
sql_delete = "DELETE FROM produtos WHERE id_produto = ?"
cursor.execute(sql_delete, (1, ))
conn.commit()
conn.close()
print("Remoção de dados bem sucedida!")
print()