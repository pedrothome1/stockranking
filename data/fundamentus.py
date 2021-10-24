import requests
from decimal import Decimal
from bs4 import BeautifulSoup

URL = 'https://fundamentus.com.br/resultado.php'
HEADERS = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}

def get_banks_tickers():
  url = URL
  headers = HEADERS
  params = {
    'segmento': 33
  }
  
  res = requests.get(url=url, headers=headers, params=params)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')
  tr_list = soup.find('tbody').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [x[0] for x in tr_list]

def get_insurance_companies_tickers():
  url = URL
  headers = HEADERS
  params = {
    'segmento': 54
  }
  
  res = requests.get(url=url, headers=headers, params=params)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')
  tr_list = soup.find('tbody').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [x[0] for x in tr_list]

def get_stocks():
  url = URL
  headers = HEADERS
  data = {
    'negociada': 'ON',
    'ordem': 1,
    'x': 33,
    'y': 13
  }
  
  res = requests.post(url=url, headers=headers, data=data)

  if res.status_code >= 400:
    return []

  soup = BeautifulSoup(res.text, 'html.parser')
  tr_list = soup.find('table').find_all('tr')
  tr_list = [[x.text for x in tr.find_all('td')] for tr in tr_list]

  return [{
    'ticker': x[0],
    'volume': Decimal(x[17].replace('.', '').replace(',', '.')),
    'evebit': Decimal(x[10].replace('.', '').replace(',', '.')),
  } for x in tr_list if x != []]

if __name__ == '__main__':
  import simplejson as json
  print(json.dumps(get_stocks(), indent=2))
