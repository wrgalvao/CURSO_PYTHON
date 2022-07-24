dados_cidade = {
    'nome': 'maraba',
    'estado': 'para',
    'area': '1000',
    'populacao': '100000'
}
dados_cidade['pais'] = 'Brasil'   #adiciona um novo par de dados ao dicionario
print(dados_cidade['nome'])   #como acessar o dicionario em uma posicao especifica
dados_cidade['nome'] = 'santos'   #altera a posiccao nome para santos
print(dados_cidade)
dados_cidade2 = dados_cidade.copy()
dados_cidade2['nome'] = 'maraba'
print(dados_cidade)
print(dados_cidade2)

novos_dados = {
    'fundacao': '25/10/2022',
    'populacao': '100'
}
dados_cidade2.update(novos_dados)   #adiciona novos valores e atualiza valores existentes no dicionario com o metodo update()
print(dados_cidade2)
valor = dados_cidade2.get('nome')   #metodo de acesso a uma posicao do dicionario
print(valor)

print(dados_cidade.keys())   #retorna uma lista de chaves de um dicionario
print(dados_cidade.values())   #retorna de valores de um dicionario
print(dados_cidade.items())   #retorna uma lista de tuplas (chave, valor) de um dicionario
