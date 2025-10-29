# Criar um código que consuma um api de clima e informe a tem´peratura e a descrição do clima em um lugar especifico



#1 etapa
# definir chave de API e o link da requisição
import requests

api_key = '2a1ac38a32354cb7b19133643251408'
cidade = input('DIgite o nome da cidade: ').strip()
url = 'https://api.weatherapi.com/v1/current.json'

# 2 - parametros da requisição
parametros ={
    'key':api_key,
    'q':cidade,
    'lang':'pt' # define a lingua da resposta como porrtugês
}

# 3- fazer a requisição
resposta = requests.get(url, params=parametros) # utilizamos o metodo get e informamos os parâmetros da requisição

#4- Verificar se a requesição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json() # convertendo a resposta json em um dicionario py
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'temperatura da cidade {cidade} é {temperatura}°c.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição {resposta.status_code}')
    print({resposta.content})