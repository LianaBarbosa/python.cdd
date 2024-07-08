import mysql.connector
banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'aulafinal'
)

print(" [1] - mostrar alunos \n [2] - Inserir novo aluno \n [3] - Encerrar programa")
opcao = int(input("insira a numeração de acordo com o quer fazer: "))

while True:

    if opcao == 1 :
      meucursor = banco.cursor()
      pesquisa = 'select * from alunos;'
      meucursor.execute(pesquisa)
      resultado = meucursor.fetchall()
      for x in resultado:
          print(x)


    elif opcao == 2:
      nome = str(input('insira seu nome: '))
      telefone = int(input(' insira seu numero de telefone: '))
      meucursor = banco.cursor()
      sql = 'INSERT INTO alunos (nome, telefone) VALUES (%s, %s)'
      data = (nome, telefone)
      meucursor.execute(sql, data)

      banco.commit()

    elif opcao == 3:
      meucursor = banco.cursor()
      meucursor.close()
      banco.close()
      print('Programa encerrado.')
    break



