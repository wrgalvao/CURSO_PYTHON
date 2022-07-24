import requests
url = 'https://api.exchangerate-api.com/v6/latest'

#REALIZANDO UMA REQUISICAO COM O METODO requests.get()
requisicao = requests.get(url)
print(requisicao.status_code)
dados = requisicao.json()
print(dados)
valor_real = float(input("Informe o valor em Reais R$ a ser convertido\n"))
cotacao = float(dados['rates']['BRL'])
valorDolar = valor_real / cotacao
print("O valor em real e:", valorDolar)