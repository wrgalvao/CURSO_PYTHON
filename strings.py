empresa = 'google'
frase = 'O PROFESSOR MANELAO THE GAME DISSE : " HOJE A PIZZA E POR MINHA CONTA"'
print(frase)
print(empresa[0])
nomes_cidades = "BELEM, BRASILIA, GOIANIA, SAO PAULO, RIO DE JANEIRO"
nomes_cidades2 = nomes_cidades.split(',')   #coloca cada cidade separadamente que estao sendo diferenciadas por virgulas por meio do metodo spli()
print(nomes_cidades2)
cabecalho = "               MENU PRINCIPAL                    "
cabecalhoNovo = cabecalho.strip()   #tira os espacos antes e depois da string por meio do metodo strip()
print(cabecalhoNovo)

cidade = "rIo De jaNeiRo"
cidadeNova = cidade.lower()
cidadeNova2 = cidade.upper()
cidadeNova3 = cidade.capitalize()
cidadeNova4 = cidade.title()
print(cidadeNova)
print(cidadeNova2)
print(cidadeNova3)
print(cidadeNova4)

print("Qual e o nome da sua cidade ?\n")
repostaUsuario = input("digite aqui o nome\n")
repostaUsuario.split()
repostaUsuario.lower()
if(repostaUsuario == 'maraba'):
    print("resposta correta")
else:
    print("resposta incorreta")

mensagem  = 'voce viu o que o warley disse na sala hoje ?'
citacao  = 'warley' in mensagem
print(citacao)
nome = "warley"
idade  = 23
filhos = 0
print(nome, "tem", idade, "anos de idade e", filhos, "filhos")
gasolina_preco = 6.705
print('{} tem {} anos de idade e {} filhos'.format(nome, idade, filhos))   #metodo format para dados externos
print("o preco da gasolina esta {:.2f}".format(gasolina_preco))