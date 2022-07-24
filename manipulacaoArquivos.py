#PROCESSO DE ABERTURA DE ARQUIVOS
arquivo = open('domCasmurro.txt', 'r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()
#PROCESSO DE ABERTURA DE ARQUIVOS


#LENDO LINHA POR LINHA POR MEIO DO METODO readline()
arquivo = open('domCasmurro.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()
#LENDO LINHA POR LINHA POR MEIO DO METODO readline()


#ABRINDO O ARQUIVO POR MEIO DO FOR
arquivo = open('domCasmurro.txt', 'r', encoding='utf-8')
for i in arquivo:
    print(i, end='')
arquivo.close()
#ABRINDO O ARQUIVO POR MEIO DO FOR


#ABRINDO ARQUIVO COM WIDHT QUE NAO PRECISA DE CLOSE()
with open('domCasmurro.txt', 'r', encoding='utf-8') as arquivo:
    texto3 = arquivo.read()
    print(texto3)
#ABRINDO ARQUIVO COM WIDHT QUE NAO PRECISA DE CLOSE()


#ESCREVENDO NO ARQUIVO COM O PYTHON
with open('arquivoTeste.txt', 'w', encoding='utf-8') as textoManipulado:
    textoManipulado.write('ESSA E UMA LINHA QUE EU ESCREVI USANDO PYTHON\n')
    textoManipulado.write('ESSA E A SEGUNDA LINHA QUE EU ESCREVI USANDO PYTHON\n')
#ESCREVENDO NO ARQUIVO COM O PYTHON



#ADICIONANDO LINHAS NO ARQUIVO COM PYTHON
with open('arquivoTeste.txt', 'a', encoding='utf-8') as textoManipulado:
    textoManipulado.write('ESSA E A TERCEIRA LINHA QUE EU ESCREVI USANDO PYTHON ADICIONANDO A LINHA\n')
#ADICIONANDO LINHAS NO ARQUIVO COM PYTHON
