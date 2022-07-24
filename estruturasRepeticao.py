contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "Item Limpo")
    else:
        print(contador, "Itens Limpos")
print("FIM DO LOOP")

senhadef = 'letscode'
senha = input("Digite uma senha\n")
while senhadef != senha:
    senha = input("Senha incorreta digite novamente\n")
print("Fim da repeticao")
