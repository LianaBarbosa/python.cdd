
import mysql.connector
#conexão com o banco de dados

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'aulafinal'
)


meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)

#fetchall recebe tudo da pesquisa e recebe em tupla
#laço de repetição  para percorrer todos os itens da lista, essa lista é de dados que estão no banco

resultado = meucursor.fetchall()
for x in resultado:
    print(x)

#inserir dados no banco

nome1='menino ney'
telefone1='111111111'
cursor = banco.cursor()
sql = 'INSERT INTO alunos (nome, telefone) VALUES (%s, %s)'
data = (nome1, telefone1)
meucursor.execute(sql, data)
banco.commit()

#menu


#meucursor.close()
#banco.close()
