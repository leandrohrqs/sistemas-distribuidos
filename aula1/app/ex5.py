import requests
from datetime import datetime
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if (r.status_code == 200):
    with open('ex5-pasta/request.txt', 'w') as arquivo:
        arquivo.write(r.text)
else:
    print('Nao houve sucesso na requisicao.')
