from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from time import sleep
from PyQt5 import QtGui

class usuario():
    login = str
    senha = str
    def __init__ (self,login,senha):
        self.login = login
        self.senha = senha
    def __str__(self):
        return str(self.login,self.senha)

class Produtos():
    codigo = int
    nome = None
    preco = float
    def __init__ (self,codigo,nome,preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return str(self.codigo)

#PRIMEIRA TELA-------------------------------------------------------------------------------

def usu ():
    logind = str(principal_tela.Login.text())
    senhad = str(principal_tela.Senha.text())
    user = usuario(logind, senhad)
    global listaG
    global listaV 
    global lista_prod
    listaV=[]
    listaG=[]
    lista_prod=[]
    carregar_g()
    carregar_v()
    carregar_p()

    ger = False
    vend = False

    for x in listaG:
        print('Estou na lista de Gerentes')
        if x.login == logind and x.senha == senhad:
            ger = True
    for x in listaV:
        print('Estou na lista de Vendedores')
        if x.login == logind and x.senha == senhad:
            vend = True

    analisando()
    sleep(1)

    if ger == True:
        print('Verificando Ger')
        gerentelogado()
        principal_tela.hide()
        gerente.show()
        principal_tela.Login.setText('')
        principal_tela.Senha.setText('')
    elif vend == True:
        print('Verificando Vendedor')
        vendedorlogado()    
        principal_tela.hide()
        tela_vendedor.show()
        principal_tela.Login.setText('')
        principal_tela.Senha.setText('')
    elif vend == False and ger == False:
        print('Deu tudo errado ')
        principal_tela.Login.setText('')
        principal_tela.Senha.setText('')
        error1()
    else:
        print('111')   
    return




def gerentelogado():
    alert = QMessageBox()
    alert.setText('Gerente Logado')
    alert.exec_()
    return


def vendedorlogado():
    alert = QMessageBox()
    alert.setText('Vendedor Logado')
    alert.exec_()
    return

#popup----------------------------------------------------------------------------------------

def error1():
    alert = QMessageBox()
    alert.setText('\tERROR 01\nUSUARIO NÃO CADASTRADO ')
    alert.exec_()
    return

def analisando():
    alert = QMessageBox()
    alert.setText('ANALISANDO INFORMAÇÕES \nPOR FAVOR AGUARDE...')
    alert.exec_()
    return

def error2():
    alert = QMessageBox()
    alert.setText('\tERROR 02\nUSUARIO JÁ CADASTRADO\nTENTE OUTRO USUARIO')
    alert.exec_()
    return

def limpo():
    alert = QMessageBox()
    alert.setText('CARRINHO ESVAZIADO')
    alert.exec_()
    return

def limparv():
    global totalv
    totalv = 0
    print (total)
    limpo()
    vendedor_venda.CarrinhoCodigo.setText("")
    vendedor_venda.valortotal.setText(str(0.0))   
    return

def limparg():
    global total
    total = 0
    print (total)
    limpo()
    venda_tela.CarrinhoCodigo.setText("")
    venda_tela.valortotal.setText(str(0.0))   
    return

def ger_cd():
    alert = QMessageBox()
    alert.setText('\tGERENTE\nCADASTRADO COM SUCESSO ')
    alert.exec_()
    return

def vend_cd():
    alert = QMessageBox()
    alert.setText('\tVENDEDOR\nCADASTRADO COM SUCESSO ')
    alert.exec_()
    return

def produto_cadastrado():
    alert = QMessageBox()
    alert.setText('Produto cadastrado com Sucesso!')
    alert.exec_()
    return

def erro_cadastro():
    alert = QMessageBox()
    alert.setText('Produto já cadastrado')
    alert.exec_()
    cadastro_tela.CadastroCodigo.setText("")
    cadastro_tela.CadastroNome.setText("")
    cadastro_tela.CadastroPreco.setText("")
    return
#popup-----------------------------------------------------------------------------------------

#definições------------------------------------------------------------------------------------

def carregar_g():
    #gerente carregar
    global listaG
    lgerente = open("1Gerentes.txt", "r")
    linhasg = lgerente.readlines() 
    for item in linhasg:
        item = item.replace("\n", "")
        item = item.split(':')
        print(item)
        g = usuario(item[0], item[1])
        listaG.append(g)
    lgerente.close()
    return

def carregar_v():
    #vendedor carregar
    global listaV
    lvendedor = open("1Vendedores.txt", "r")
    linhasv = lvendedor.readlines()
    for item in linhasv:
        item = item.replace("\n", "")
        item = item.split(':')
        v = usuario(item[0], item[1])
        listaV.append(v)
    lvendedor.close()
    return
def carregar_p():
    #produtos Carregar
    global lista_prod
    lprodutos = open("1Produtos.txt", "r")
    linhasp = lprodutos.readlines()
    for item in linhasp:
        item = item.replace("\n", "")
        item = item.split(':')
        p = Produtos(int(item[0]), item[1], float(item[2]))
        lista_prod.append(p)
    lprodutos.close()
    return


#---------------------------------------------------------------------------------------------------------

def salvar_usuarios():
    sg = open('1Gerentes.txt', 'w')
    sv = open('1Vendedores.txt', 'w')
    global listaV
    global listaG
    for item in listaG:
        sg.write('{}:{}\n'.format(item.login, item.senha))
    for item in listaV:
        sv.write('{}:{}\n'.format(item.login, item.senha))
    sleep(1)
    sv.close()
    sg.close()
    return


def salvar_produtos():
    sp = open('1Produtos.txt', 'w')
    global lista_prod
    for item in lista_prod:
        sp.write('{}:{}:{}\n'.format(item.codigo,item.nome,item.preco))
    sleep(1)
    sp.close()
    return

#gerencia--------------------------------------------------------------------------------------------
def cadastrarg ():
    loging = str(gerente.cad_login.text())
    senhag = str(gerente.cad_senha.text())
    new_g = usuario(loging, senhag)
    global listaG
    coco = 0
    for x in listaG:
        if x.login == loging:
           coco = 1 
    analisando()
    sleep(1.3)
    if coco == 0:
        listaG.append(new_g)
        ger_cd()
        gerente.cad_login.setText('')
        gerente.cad_senha.setText('')
    else: 
        error2()
    return

def cadastrovend():
    loginv = str(gerente.cad_login.text())
    senhav = str(gerente.cad_senha.text())
    new_v = usuario(loginv, senhav)
    global listaV
    coco = 0
    for x in listaV:
        if x.login == loginv:
           coco = 1
    analisando()
    sleep(1.3)
    if coco == 0:
        listaV.append(new_v)
        vend_cd()
        gerente.cad_login.setText('')
        gerente.cad_senha.setText('')
    else:
        error2() 
    return


#----------------------------------------------------------------


def vendido():
    cod_digitado = int(venda_tela.CarrinhoCodigo.text())
    venda_tela.valortotal.setText(str(0.0))
    global total
    for x in lista_prod:        
        if x.codigo == cod_digitado:            
            venda_tela.LISTA.setText('|CODIGO {} |\n| NOME {} |\n| PREÇO {}|'.format(x.codigo,x.nome,x.preco))
            p = int(venda_tela.quantidade.text())
            if p != 0 :
                total += float(x.preco*int(venda_tela.quantidade.text())) 
                venda_tela.valortotal.setText(str(total))
                venda_tela.CarrinhoCodigo.setText("")
                venda_tela.quantidade.setText("1")
            if p == 0 :
                venda_tela.valortotal.setText('NDA')
                venda_tela.quantidade.setText("1")
                venda_tela.CarrinhoCodigo.setText("")
    return

def vendidovoltargerente():
    venda_tela.valortotal.setText("")
    venda_tela.quantidade.setText("")
    venda_tela.CarrinhoCodigo.setText("")
    venda_tela.hide()
    sleep(0.1)
    gerente.show()
    return

def mostrarvendasgerente():
    gerente.hide()
    sleep(0.1)
    venda_tela.show()
    return

def mostartc():
    gerente.hide()
    sleep(0.1)
    cadastro_tela.show()
    return
    
def voltargerencia():
    cadastro_tela.hide()
    sleep(0.1)
    gerente.show()

    return

#-----------------------------------------------------------------------------------------

def cadastro_de_item():
    codigo = cadastro_tela.CadastroCodigo.text()
    codigodigitado = int(cadastro_tela.CadastroCodigo.text())
    nome = cadastro_tela.CadastroNome.text()
    preco = cadastro_tela.CadastroPreco.text()
    novo = Produtos(int(codigo),nome,float(preco))
    global codigoss
    global lista_prod
    vv = 0
    for item in lista_prod:
        if item.codigo == codigodigitado:
            vv = 1
    analisando()
    sleep(0.5)
    if vv == 0:
        codigoss.append(codigo)
        lista_prod.append(novo)
        print(lista_prod)
        produto_cadastrado()
        cadastro_tela.CadastroCodigo.setText("")
        cadastro_tela.CadastroNome.setText("")
        cadastro_tela.CadastroPreco.setText("")
    elif vv==1:
        erro_cadastro()
    else:
        print('q')

    return


def gerentesaiu():
    gerente.hide()
    sleep(0.1)
    principal_tela.show()
    gerente.cad_login.setText('')
    gerente.cad_senha.setText('')
    salvar_produtos()
    salvar_usuarios()
    global lista_prod
    global listaV
    global listaG
    lista_prod = []
    listaV = []
    listaG = []
    return

#gerencia acaba ----------------------------------------------------------------------------------


#vendedor-------------------------------------------------------------------------------------------

def mostrarvendas():
    tela_vendedor.hide()
    vendedor_venda.show()
    return

def vendido_vendedor():    
    cod_digitado = int(vendedor_venda.CarrinhoCodigo.text())
    vendedor_venda.valortotal.setText(str(0.0))
    global totalv
    for x in lista_prod:        
        if x.codigo == cod_digitado:            
            vendedor_venda.LISTA.setText('|CODIGO {} |\n| NOME {} |\n| PREÇO {}|'.format(x.codigo,x.nome,x.preco))
            p = int(vendedor_venda.quantidade.text())
            
            if p != 0 :
                totalv += float(x.preco*(p)) 
                vendedor_venda.valortotal.setText(str(totalv))
                vendedor_venda.CarrinhoCodigo.setText("")
                vendedor_venda.quantidade.setText("1")

            if p == 0 :
                vendedor_venda.valortotal.setText('NDA')
                vendedor_venda.quantidade.setText("1")
                vendedor_venda.CarrinhoCodigo.setText("")
    return


#----------------------------------------------------------------------------------------------------


def deslogarvendedor():
    tela_vendedor.hide()
    sleep(0.1)
    principal_tela.show()
    global totalv
    global lista_prod
    global listaV
    global listaG
    totalv=0
    lista_prod = []
    listaV = []
    listaG = []
    return

def vendidosairvendedor():
    vendedor_venda.valortotal.setText('00')
    vendedor_venda.quantidade.setText("1")
    vendedor_venda.CarrinhoCodigo.setText("")
    vendedor_venda.hide()
    sleep(0.1)
    tela_vendedor.show()
    global totalv
    totalv=0
    return




#vendedor acaba -------------------------------------------------------------------------------------------


#Variables

app = QtWidgets.QApplication([])
cadastro_tela = uic.loadUi("Cadastro.ui")
venda_tela = uic.loadUi("Venda.ui")
principal_tela = uic.loadUi("Menu.ui")
gerente = uic.loadUi("Gerencia.ui")
tela_vendedor = uic.loadUi("telavennd.ui")
vendedor_venda = uic.loadUi("VENDAVENDEDOR.ui")

#Connections Menu
principal_tela.Confirmar.clicked.connect(usu)

#Connections VENDEDOR
vendedor_venda.ProximoVenda.clicked.connect(limparv)
vendedor_venda.Voltar.clicked.connect(vendidosairvendedor)
vendedor_venda.CarrinhoAdicionar.clicked.connect(vendido_vendedor)
vendedor_venda.Voltar.clicked.connect(vendidosairvendedor)

#tela vendedor
tela_vendedor.tela_vendedor_vender.clicked.connect(mostrarvendas)
tela_vendedor.sair.clicked.connect(deslogarvendedor)

# Connections Gerencia
gerente.cadastrar_ger.clicked.connect(cadastrarg)
gerente.cadastrar.clicked.connect(cadastrovend)
gerente.tela_venda.clicked.connect(mostrarvendasgerente)
gerente.tela_cadastro.clicked.connect(mostartc)
gerente.sair.clicked.connect(gerentesaiu)

# Connections Sell
venda_tela.Voltar.clicked.connect(vendidovoltargerente)
venda_tela.CarrinhoAdicionar.clicked.connect(vendido)
venda_tela.ProximoVenda.clicked.connect(limparg)

# Connections Cad

cadastro_tela.Voltar.clicked.connect(voltargerencia)
cadastro_tela.CadastroCadastrar.clicked.connect(cadastro_de_item)


#Global

codigoss = []
total = 0
totalv = 0
lista_prod = []
listaV = []
listaG = []

#Show
principal_tela.show()
app.exec()