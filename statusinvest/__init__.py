from util import ETFS, FIIS

BROKER = 'NU INVEST CORRETORA DE VALORES'

def get_asset_category(ticker: str):
  if ticker in ETFS:
    return "ETF's"
  if ticker in FIIS:
    return "FII's"
  return 'Ações'
