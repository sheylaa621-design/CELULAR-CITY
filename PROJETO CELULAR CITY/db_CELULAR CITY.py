import mysql.connector
from mysql.connector import Error
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            password = '',
            database = 'db_CELULAR_CITY',
            user = 'root'   )
        
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banca de dados")
            return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados: {}".format(e))
def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
        print("Conexão ao banco de dados fechada")
if __name__ == "__main__":
    conexao = criar_conexao()
    if  conexao:
        fechar_conexao(conexao)

 