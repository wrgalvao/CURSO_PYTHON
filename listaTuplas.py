nomes_paises = ['BRASIL', 'ARGENTINA', 'CHINA', 'CANADA', 'JAPAO']
print(nomes_paises)
print("TAMANHO DA LISTA E IGUAL A", len(nomes_paises))   #imprime o tamanho da lista com a funcao len()
print("PAIS NA POSICAO 4 E:", nomes_paises[4])   #imprime na tela o pais da posicao 4 da lista de nomes_paises
nomes_paises[4] = 'COLOMBIA'
print("PAIS NA POSICAO 4 AGORA E:", nomes_paises[4])
print(nomes_paises[::2])   #mostra na tela paises da lista pulando de 2 em 2
print("BRASIL" in nomes_paises)

lista_capitais = []
lista_capitais.append('BRASILIA')   #adiciona uma capital na lista de capitais com o metodo append()
lista_capitais.append('GOIANIA')
lista_capitais.append('BELÉM')
lista_capitais.append('SÃO PAULO')
lista_capitais.append('RIO DE JANEIRO')
print(lista_capitais)
lista_capitais.insert(2, 'CURITIBA')   #adiciona a capital curitiba na posicao 2 da lista com o metodo insert()
print(lista_capitais)
lista_capitais.remove('CURITIBA')   #remove curitiba da lista de capitais por meio do metodo remove()
print(lista_capitais)
lista_capitais.pop(1)   #remove a capital da posicao 1 da lista de capitais por meio do metodo pop()
print(lista_capitais)

#--------------------------------------AQUI COMEÇA TUPLAS----------------------------------------------
#tuplas nao permite alterações no array, como adicionar, ou alterar valores
nomes_paises_segunda = ('FRANÇA', 'INGLATERRA', 'COREIA DO SUL', 'PORTUGAL', 'PARAGUAI')
print(nomes_paises_segunda)
a, b, c, d, e = nomes_paises_segunda   #listas nao permite realizar essa operacao
print(a, b, c, d, e)
