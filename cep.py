import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'aulafinal')

cep = input('digite seu cep:')
link = f'http://viacep.com.br/ws{cep}/json/'
requisicao = request.get(get)
endereco = requisicao.json()
cep1 = endereco['cep']
logradouro = endereco['logradouro']




