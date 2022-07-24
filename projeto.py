import csv
import requests
import datetime as data
from PIL import Image
from IPython.display import display

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

url = 'https://api.covid19api.com/dayone/country/brazil'
requisicao = requests.get(url)
dados = requisicao.json()
dadosFinal = []
for i in dados:
    dadosFinal.append([i['Confirmed'], i['Deaths'], i['Recovered'], i['Active'], i['Date']])
print(dadosFinal)
dadosFinal.insert(0, ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])

for i in range(1, len(dadosFinal)):
    dadosFinal[i][DATA] = dadosFinal[i][DATA][:10]

print(data.date(2022, 7, 17))  #ano, mes e dia
print(data.datetime (2022, 7, 17, 18, 54, 20, 7))   #ano, mes, dia, hora, minutos, segundo e microsegundo
print(data.time(18, 54, 30))   #hora, minutos e segundo

with open('brasil_covid.csv', 'w', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerow(dadosFinal)

for i in range(1, len(dadosFinal)):
    dadosFinal[i][DATA] = data.datetime.strptime(dadosFinal[i][DATA], '%Y-%m-%d')
print(dadosFinal)

def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]
def setTitulo(titulo = ''):
    if titulo != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'titulo': titulo,
        'display': display
    }
def createChart(x, y, labels, kind = 'bar', title = ''):
    datasets = get_datasets(y,labels)
    options = setTitulo(title)
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart
def get_api_chart(chart):
    url = 'https://quickchart.io/chart'
    resposta = requests.get('f{url}?c={str(chart)}')
    return resposta.content
def save_imagem(path, content):
    with open(path, 'wb', encoding='utf-8') as imagem:
        imagem.write(content)
def mostra_imagem(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in dadosFinal[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in dadosFinal[1::10]:
    y_data_2.append(obs[RECUPERADOS])
lables = ['Confirmados', 'Recuperados']


x = []
for obs in dadosFinal[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = createChart(x, [y_data_1, y_data_2], lables, title='GRAFICO CONFIRMADOS VS RECUPERADOS')
chart_content = get_api_chart(chart)
save_imagem('meuPrimeiroGrafico.png', chart_content)
mostra_imagem('meuPrimeiroGrafico.png')