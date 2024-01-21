from datetime import datetime
import coin
from binance.client import Client
import apikey

# BALANCE EN LA BILLETERA EN CRIPTO
client = Client(apikey.API_KEY, apikey.API_SECRET, tld='com')
symbol = coin.cripto+"USDT"
balanceCripto = client.get_account()

ada = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "ADA"]
ada = float(ada[0])
info_ada = client.get_avg_price(symbol='ADAUSDT')
precio_ada = float(info_ada['price'])
usdt_ada = ada * precio_ada

bnb = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "BNB"]
bnb = float(bnb[0])
info_bnb = client.get_avg_price(symbol='BNBUSDT')
precio_bnb = float(info_bnb['price'])
usdt_bnb = bnb * precio_bnb

btc = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "BTC"]
btc = float(btc[0])
info_btc = client.get_avg_price(symbol='BTCUSDT')
precio_btc = float(info_btc['price'])
usdt_btc = btc * precio_btc

eth = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "ETH"]
eth = float(eth[0])
info_eth = client.get_avg_price(symbol='ETHUSDT')
precio_eth = float(info_eth['price'])
usdt_eth = eth * precio_eth

link = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "LINK"]
link = float(link[0])
info_link = client.get_avg_price(symbol='LINKUSDT')
precio_link = float(info_link['price'])
usdt_link = link * precio_link

ltc = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "LTC"]
ltc = float(ltc[0])
info_ltc = client.get_avg_price(symbol='LTCUSDT')
precio_ltc = float(info_ltc['price'])
usdt_ltc = ltc * precio_ltc

matic = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "MATIC"]
matic = float(matic[0])
info_matic = client.get_avg_price(symbol='MATICUSDT')
precio_matic = float(info_matic['price'])
usdt_matic = matic * precio_matic

neo = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "NEO"]
neo = float(neo[0])
info_neo = client.get_avg_price(symbol='NEOUSDT')
precio_neo = float(info_neo['price'])
usdt_neo = neo * precio_neo

rune = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "RUNE"]
rune = float(rune[0])
info_rune = client.get_avg_price(symbol='RUNEUSDT')
precio_rune = float(info_rune['price'])
usdt_rune = rune * precio_rune

sol = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "SOL"]
sol = float(sol[0])
info_sol = client.get_avg_price(symbol='SOLUSDT')
precio_sol = float(info_sol['price'])
usdt_sol = sol * precio_sol

theta = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "THETA"]
theta = float(theta[0])
info_theta = client.get_avg_price(symbol='THETAUSDT')
precio_theta = float(info_theta['price'])
usdt_theta = theta * precio_theta

waves = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "WAVES"]
waves = float(waves[0])
info_waves = client.get_avg_price(symbol='WAVESUSDT')
precio_waves = float(info_waves['price'])
usdt_waves = waves * precio_waves

xrp = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "XRP"]
xrp = float(xrp[0])
info_xrp = client.get_avg_price(symbol='XRPUSDT')
precio_xrp = float(info_xrp['price'])
usdt_xrp = xrp * precio_xrp


total_usdt_criptos = usdt_ada + usdt_btc + usdt_eth + usdt_bnb + usdt_link + usdt_ltc + usdt_matic + usdt_neo + usdt_rune + usdt_sol + usdt_theta + usdt_waves + usdt_xrp

usdt = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "USDT"]
usdt = float(usdt[0])

print(f"ADA = {ada:.5f}")
print(f"usdt ada = {usdt_ada:.5f}")
print(f"BNB = {bnb:.5f}")
print(f"usdt bnb = {usdt_bnb:.5f}")
print(f"BTC = {btc:.5f}")
print(f"usdt btc = {usdt_btc:.5f}")
print(f"ETH = {eth:.5f}")
print(f"usdt eth = {usdt_eth:.5f}")
print(f"LINK = {link:.5f}")
print(f"usdt link = {usdt_link:.5f}")
print(f"LTC = {ltc:.5f}")
print(f"usdt ltc = {usdt_ltc:.5f}")
print(f"MATIC = {matic:.5f}")
print(f"usdt matic = {usdt_matic:.5f}")
print(f"NEO = {neo:.5f}")
print(f"usdt neo = {usdt_neo:.5f}")
print(f"RUNE = {rune:.5f}")
print(f"usdt rune = {usdt_rune:.5f}")
print(f"SOL = {sol:.5f}")
print(f"usdt sol = {usdt_sol:.5f}")
print(f"THETA = {theta:.5f}")
print(f"usdt theta = {usdt_theta:.5f}")
print(f"WAVES = {waves:.5f}")
print(f"usdt waves = {usdt_waves:.5f}")
print(f"XRP = {xrp:.5f}")
print(f"usdt xrp = {usdt_xrp:.5f}")
print(f"USDT = {usdt:.2f}")
print(f"total usdt en criptos = {total_usdt_criptos:.5f}")
print(f"total de usdt = {usdt + total_usdt_criptos:.2f}")

# SISTEMA DE FUCHA
date = datetime.now()
year_month = date.strftime('%m %Y')
with open(f"{year_month} cartera.txt", "a") as TextIOWrapper:
    TextIOWrapper.write(f'<-[{date}]-[{coin.user}]-\n-[TOTAL USDT = {usdt + total_usdt_criptos:.2f}]\n-[USDT = {usdt:.5f}]\n-[ADA = {usdt_ada:.5f}]\n-[BNB = {usdt_bnb:.5f}]\n-[BTC = {usdt_btc:.5f}]\n-[ETH = {usdt_eth:.5f}]\n-[LINK = {usdt_link:.5f}]\n-[LTC = {usdt_ltc:.5f}]\n-[MATIC = {usdt_matic:.5f}]\n-[NEO = {usdt_neo:.5f}]\n-[RUNE = {usdt_rune:.5f}]\n-[SOL = {usdt_sol:.5f}]\n-[THETA = {usdt_theta:.5f}]\n-[WAVES = {usdt_waves:.5f}]\n-[XRP = {usdt_xrp:.5f}]->\n-------------------------------------------------------------\n')