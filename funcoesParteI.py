#corpo basico de uma funcao
mensagem = 'hello world'
def hello (mensagem):
    print(mensagem)
#corpo basico de um funcao
def media(valor, valor2):
    media = (valor + valor2) / 2
    return media
valor = input("digite o primeiro valor\n")
valor = float(valor)
valor2 = input("digite o segundo valor\n")
valor2 = float(valor2)
media = media(valor, valor2)
print(media)
