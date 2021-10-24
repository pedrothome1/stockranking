import requests
from decimal import Decimal
from bs4 import BeautifulSoup

URL = 'https://www.investsite.com.br/selecao_acoes.php'
HEADERS = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}

def get_banks_tickers():
  url = 'https://www.investsite.com.br/selecao_acoes_financ.php'
  headers = HEADERS
  data = {
    'num_result': 'todos',
    'todos': 'todos',
    'setor': 'Financeiro',
    'subsetor': 'Intermediários Financeiros',
    'segmento': 'Bancos'
  }
  
  res = requests.post(url=url, headers=headers, data=data)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')

  tr_list = soup.find(id='tabela_selecao_acoes_financ').find('tbody').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [x[0] for x in tr_list]

def get_insurance_companies_tickers():
  url = URL
  headers = HEADERS
  data = {
    'num_result': 'todos',
    'setor': 'Financeiro',
    'subsetor': 'Previdência e Seguros',
    'segmento': 'Seguradoras',
  }
  
  res = requests.post(url=url, headers=headers, data=data)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')

  tr_list = soup.find(id='tabela_selecao_acoes').find('tbody').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [x[0] for x in tr_list]

def get_stocks():
  url = URL
  headers = HEADERS
  data = {
    'num_result': 'todos',
  }
  
  res = requests.post(url=url, headers=headers, data=data)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')

  tr_list = soup.find(id='tabela_selecao_acoes').find('tbody').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [{
    'ticker': x[0],
    'volume': Decimal(x[25].replace('.', '').replace(',', '.')) if x[25] != 'NA' else 'NA',
    'evebit': Decimal(x[22].replace('.', '').replace(',', '.')) if x[22] != 'NA' else 'NA',
  } for x in tr_list]

if __name__ == '__main__':
  import simplejson as json
  print(json.dumps(get_insurance_companies_tickers(), indent=2))
