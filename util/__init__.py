import math
from decimal import Decimal

ETFS = ['IVVB11', 'IMAB11']
FIIS = [
  'BTLG11',
  'MCCI11',
  'PVBI11',
  'RBRP11',
  'RECR11',
  'HGRU11',
  'MALL11',
  'XPLG11',
  'HGLG11',
  'VGIP11',
  'ALZR11',
  'VRTA11',
  'VISC11',
  'VILG11',
  'XPML11',
  'IRDM11',
]

B3_TRADING_FEE = Decimal('0.00005')
B3_SETTLEMENT_FEE = Decimal('0.00025')

def round(value: Decimal):
  return Decimal(math.floor(value * 100)) / 100

def get_total_fee(value: Decimal):
  trading_fee = round(value * B3_TRADING_FEE)
  settlement_fee = round(value * B3_SETTLEMENT_FEE)
  return trading_fee + settlement_fee

def money_in_decimal(money: str):
  money = money.strip('R$ ').replace('.', '').replace(',', '.')
  return Decimal(money)

def normalize_ticker(ticker: str):
  ticker = ticker.strip()
  return ticker[:-1] if ticker.endswith('F') else ticker

if __name__ == '__main__':
  print('\n============= round =============')
  print(round(Decimal('0.45698')))
  print(type(round(Decimal('0.45698'))))

  print('\n============= money_in_decimal =============')
  print(money_in_decimal('R$ 315,56'))
  print(type(money_in_decimal('R$ 315,56')))

  print('\n============= normalize_ticker =============')
  print(normalize_ticker('CVCB3F'))
  print(type(normalize_ticker('CVCB3F')))

  print()
