#criando funcao com quantidade infinita de parametros para calcular a media
def media(*args):
    print(args, type(args))
    soma = sum(args)
    media = soma/len(args)
    return media
print("A media e", media(8, 9, 10))


#chamando uma funcao para criar dicionario automatizado com kwargs


def print_info(**kwargs):
    print(kwargs, type(kwargs))


print_info(nome = 'Warley', sobrenome = 'Galvao')