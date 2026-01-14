import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtCore
import mysql.connector
from PyQt5.QtWidgets import QMainWindow

banco = mysql.connector.connect(
    host = 'localhost',
    database = 'db_CELULAR_CITY',
    user = 'root',
    password = ''
)
#Aplicação principal
app = QApplication(sys.argv)
if getattr(sys,'frozen',False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

UI_FOLDER = os.path.join(base_path, 'TELAS_CELULAR_CITY')


def load_ui_relative(ui_filename):
    #Aqui está o segredo: usar UI_FOLDER em vez de os.path.dirname(__file__)
    full_path = os.path.join(UI_FOLDER, ui_filename)
    if not os.path.exists(full_path):
        # print("Erro: Arquivo UI não encontrado: {}".format(full_path))]
        print('\n --- ERRO DE LOCALIZAÇÃO ---')
        print('O python procurou em: {}'.format(full_path))
        print('Conteúdo da pasta base: {}'.format(os.liustdir(base_path)))
        return None
    return uic.loadUi(full_path)
#Conexão ao banco de dados
try:
    banco = mysql.connector.connect()
    host = 'localhost'
    database = 'db_CELULAR_CITY'
    user = 'root'
    password = ''
    print('Conexão bem sucedido ao banco de dados')

except Exception as e:
    print('Erro ao conectar ao banco de dados: {}'.format(e))


#Funções de login
def verificar_login():
    campo_login = tela_de_login.lineEdit.text()
    campo_senha = tela_de_login.lineEdit_2.text()
    if campo_login == 'Gabriel' and campo_senha == 'Gabriel14':
        # tela_de_login.label_erro_senha.setText("") #Limpa a mensagem de erro
        Tela_proprietario()
        tela_de_login.close()
        print('Bem vindo Gabriel!')
    elif campo_login == 'Alexandre' and campo_senha == 'Alexandre15':
        print("Bem vindo Alexandre!")
    else:
        #Em vez de apenas imprimr a mensagem de erro no consoe, agora ela é exibida na interface gráfica
        print('Senha inválida.')
        tela_de_login.label_erro_senha.setText('Usuário ou senha inválidas\n caso não lembre da sua senha\n entre em contato com a equipe de desenvovimento.') 
def limpar_label_error():
    tela_de_login.label_erro_senha.setText('')


#Carrengamento das telas    
# app = QApplication(sys.argv)
tela_de_login = load_ui_relative('tela_inicial_login.ui')
tela_atendente = load_ui_relative('Tela_atendente.ui')
tela_proprietario = load_ui_relative('tela_proprietario.ui')
tela_pedido_atendente = load_ui_relative('tela_pedido_atendente.ui')
# tela_formas_de_pagamento = load_ui_relative('tela_formas_de_pagamento.ui')
# tela_pedido_atendente = load_ui_relative('tela_pedido_atendente.ui')
# tela_financeiro = load_ui_relative('tela_financeiro.ui')

#Telas de editar valores no MYSQL
# tela_editar_produtos = load_ui_relative('tela_editar_produtos.ui')
# tela_listar_pedidos = load_ui_relative('tela_listar_pedidos.ui')
#Funções de INTERFACE 

def Tela_atendente():
    tela_atendente.show()
def Tela_proprietario():
    tela_proprietario.show()
# def editar_produtos():
#     tela_editar_produtos.show()
# def Tela_listar_pedidos():
#     tela_listar_pedidos.show()
# def tela_do_financeiro():
#     tela_financeiro.show()

#Configurações dos botões e execução
if tela_de_login:
    # tela_de_login.pushButton.clicked.connect(verificar_login)
    # tela_de_login.adjustSize()#Tamanho exato da tela com todos os elementos
    tela_de_login.show()
    tela_de_login.pushButton_3.clicked.connect(lambda: app.quit())
    tela_de_login.pushButton.clicked.connect(verificar_login)
    # tela_de_login.lineEdit_2.textChanged.connect(limpar_label_error)
if tela_proprietario:
    tela_proprietario.pushButton_2.clicked.connect(lambda:(tela_proprietario.close() ,tela_pedido_atendente.show()))
    tela_proprietario.pushButton.clicked.connect(lambda:(tela_proprietario.close(),tela_de_login.show()))
    #testando branch
    
    sys.exit(app.exec_())





