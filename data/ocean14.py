import requests
from decimal import Decimal

URL = 'https://www.oceans14.com.br/rendaVariavel/respostaAjax/acoesBuscaAvancada.aspx'
HEADERS = {
  'x-requested-with': 'XMLHttpRequest',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
  'origin': 'https://www.oceans14.com.br',
  'referer': 'https://www.oceans14.com.br/acoes/busca-avancada'
}

def get_banks_tickers():
  url = URL
  headers = HEADERS
  data = {
    'setor': 'Financeiro e outros',
    'subsetor': 'Intermediários financeiros',
    'segmento': 'Bancos'
  }
  
  res = requests.post(url=url, headers=headers, data=data)

  return [x['papel'] for x in res.json()] if res.status_code < 400 else []

def get_insurance_companies_tickers():
  url = URL
  headers = HEADERS
  data = {
    'setor': 'Financeiro e outros',
    'subsetor': 'Previdência e seguros',
    'segmento': 'Seguradoras'
  }

  res = requests.post(url=url, headers=headers, data=data)

  return [x['papel'] for x in res.json()] if res.status_code < 400 else []

def get_stocks():
  url = URL
  headers = HEADERS

  res = requests.post(url=url, headers=headers)

  return [{
    'ticker': x['papel'],
    'volume': Decimal(str(x['volumeDiario'])) * 1000000,
    'evebit': Decimal(str(x['evebit'])),
  } for x in res.json()] if res.status_code < 400 else []

if __name__ == '__main__':
  import simplejson as json
  print(json.dumps(get_stocks(), indent=2))
