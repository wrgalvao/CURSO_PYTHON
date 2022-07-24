import csv

#FAZENDO A LEITURA DE ARQUIVOS CSV
with open('brasil_covid.csv', 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
#FAZENDO A LEITURA DE ARQUIVOS CSV

#FAZENDO A LEITURA DE ARQUIVOS CSV
with open('brasil_covid.csv', 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)
#FAZENDO A LEITURA DE ARQUIVOS CSV

#FAZENDO ESCRITA DE DADOS EM UM ARQUIVO CSV
with open('users.csv', 'w', encoding='utf-8', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'sexo', 'nascimento'])
    escritor.writerow(['warley', 'galvao', 'masculino', '10/08/1998'])
#FAZENDO ESCRITA DE DADOS EM UM ARQUIVO CSV




def escreveDados():
    with open('exemplo.csv', 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cabecalho)
        escritor.writerow(dados)
def lerDados():
    with open('exemplo.csv', 'r', encoding='utf-8', newline='') as arquivo2:
        leitor = csv.reader(arquivo2)
        for linha in leitor:
            print(linha)


#REALIZANDO UM EXEMPLO
cabecalho = ['nome', 'sobrenome']
dados = []
resposta = 1
while resposta != '0':
    nome = input("Cadastre um nome\n")
    sobrenome = input("Cadastre um sobrenome\n")
    dados.append([nome, sobrenome])
    resposta = input("1 - continuar\n0 sair\n")
print(dados)
escreveDados()
lerDados()
#REALIZANDO UM EXEMPLO