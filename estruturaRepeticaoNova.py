nomes_cidades = ['maraba', 'belem', 'brasilia', 'sao paulo', 'rio de janeito']
cidade = {
    'cidade': 'maraba',
    'populacao': 100000,
    'estado': 'para'
}
for i in nomes_cidades:
    print(i)
#for em dicionarios
for i in cidade:
    print(' {}  {}'.format(i, cidade[i]))
for i in range(len(nomes_cidades)):
    nomes_cidades[i] = 'rio de janeiro'
print(nomes_cidades)