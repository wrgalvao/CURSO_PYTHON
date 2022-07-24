corrida = 4.30
print(type(corrida))
valorDisponivel = input("Digite o valor disponivel para a corrida\n")
valorDisponivel = float(valorDisponivel)
if valorDisponivel < corrida:
    print("VOCE PEGA O UBER")
elif valorDisponivel == corrida:
    print("O valor e igual pague a corrida")
else:
    print("Pegue o onibus")