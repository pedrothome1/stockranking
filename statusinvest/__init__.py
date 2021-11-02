from util import ETFS, FIIS

BROKER = 'EASYNVEST - TITULO CV S.A.'

def get_asset_category(ticker: str):
  if ticker in ETFS:
    return "ETF's"
  if ticker in FIIS:
    return "FII's"
  return 'Ações'
