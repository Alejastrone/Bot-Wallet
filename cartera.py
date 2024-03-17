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

agix = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "AGIX"]
agix = float(agix[0])
info_agix = client.get_avg_price(symbol='AGIXUSDT')
precio_agix = float(info_agix['price'])
usdt_agix = agix * precio_agix

algo = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "ALGO"]
algo = float(algo[0])
info_algo = client.get_avg_price(symbol='ALGOUSDT')
precio_algo = float(info_algo['price'])
usdt_algo = algo * precio_algo

avax = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "AVAX"]
avax = float(avax[0])
info_avax = client.get_avg_price(symbol='AVAXUSDT')
precio_avax = float(info_avax['price'])
usdt_avax = avax * precio_avax

btc = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "BTC"]
btc = float(btc[0])
info_btc = client.get_avg_price(symbol='BTCUSDT')
precio_btc = float(info_btc['price'])
usdt_btc = btc * precio_btc

dot = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "DOT"]
dot = float(dot[0])
info_dot = client.get_avg_price(symbol='DOTUSDT')
precio_dot = float(info_dot['price'])
usdt_dot = dot * precio_dot

eth = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "ETH"]
eth = float(eth[0])
info_eth = client.get_avg_price(symbol='ETHUSDT')
precio_eth = float(info_eth['price'])
usdt_eth = eth * precio_eth

fet = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "FET"]
fet = float(fet[0])
info_fet = client.get_avg_price(symbol='FETUSDT')
precio_fet = float(info_fet['price'])
usdt_fet = fet * precio_fet

fil = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "FIL"]
fil = float(fil[0])
info_fil = client.get_avg_price(symbol='FILUSDT')
precio_fil = float(info_fil['price'])
usdt_fil = fil * precio_fil

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

rndr = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "RNDR"]
rndr = float(rndr[0])
info_rndr = client.get_avg_price(symbol='RNDRUSDT')
precio_rndr = float(info_rndr['price'])
usdt_rndr = rndr * precio_rndr

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

xlm = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "XLM"]
xlm = float(xlm[0])
info_xlm = client.get_avg_price(symbol='XLMUSDT')
precio_xlm = float(info_xlm['price'])
usdt_xlm = xlm * precio_xlm

xrp = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "XRP"]
xrp = float(xrp[0])
info_xrp = client.get_avg_price(symbol='XRPUSDT')
precio_xrp = float(info_xrp['price'])
usdt_xrp = xrp * precio_xrp

uni = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "UNI"]
uni = float(uni[0])
info_uni = client.get_avg_price(symbol='UNIUSDT')
precio_uni = float(info_uni['price'])
usdt_uni = uni * precio_uni

total_usdt_criptos = usdt_ada + usdt_avax + usdt_btc + usdt_eth + usdt_fil + usdt_uni + usdt_rndr + usdt_fet + usdt_agix + usdt_dot + usdt_link + usdt_ltc + usdt_matic + usdt_neo + usdt_rune + usdt_sol + usdt_theta + usdt_waves + usdt_xrp

usdt = [b['free'] for b in balanceCripto['balances'] if b['asset'] == "USDT"]
usdt = float(usdt[0])

print(f"USDT = {usdt:.2f}")
print(f"total usdt en criptos = {total_usdt_criptos:.5f}")
print(f"total de usdt = {usdt + total_usdt_criptos:.2f}")
print(f"ADA = {ada:.5f}")
print(f"usdt ada = {usdt_ada:.5f}")
print(f"AGIX = {agix:.5f}")
print(f"usdt agix = {usdt_agix:.5f}")
print(f"ALGO = {algo:.5f}")
print(f"usdt algo = {usdt_algo:.5f}")
print(f"AVAX = {avax:.5f}")
print(f"usdt avax = {usdt_avax:.5f}")
print(f"BTC = {btc:.5f}")
print(f"usdt btc = {usdt_btc:.5f}")
print(f"DOT = {dot:.5f}")
print(f"usdt dot = {usdt_dot:.5f}")
print(f"ETH = {eth:.5f}")
print(f"usdt eth = {usdt_eth:.5f}")
print(f"FET = {fet:.5f}")
print(f"usdt fet = {usdt_fet:.5f}")
print(f"FIL = {fil:.5f}")
print(f"usdt fil = {usdt_fil:.5f}")
print(f"LINK = {link:.5f}")
print(f"usdt link = {usdt_link:.5f}")
print(f"LTC = {ltc:.5f}")
print(f"usdt ltc = {usdt_ltc:.5f}")
print(f"MATIC = {matic:.5f}")
print(f"usdt matic = {usdt_matic:.5f}")
print(f"NEO = {neo:.5f}")
print(f"usdt neo = {usdt_neo:.5f}")
print(f"RNDR = {rndr:.5f}")
print(f"usdt rndr = {usdt_rndr:.5f}")
print(f"RUNE = {rune:.5f}")
print(f"usdt rune = {usdt_rune:.5f}")
print(f"SOL = {sol:.5f}")
print(f"usdt sol = {usdt_sol:.5f}")
print(f"THETA = {theta:.5f}")
print(f"usdt theta = {usdt_theta:.5f}")
print(f"WAVES = {waves:.5f}")
print(f"usdt waves = {usdt_waves:.5f}")
print(f"XLM = {xlm:.5f}")
print(f"usdt xlm = {usdt_xlm:.5f}")
print(f"XRP = {xrp:.5f}")
print(f"usdt xrp = {usdt_xrp:.5f}")
print(f"UNI = {uni:.5f}")
print(f"usdt uni = {usdt_uni:.5f}")

# SISTEMA DE FUCHA
date = datetime.now()
year_month = date.strftime('%m %Y')
with open(f"{apikey.user} cartera.txt", "a") as f:
    f.write(f'<-[{date}]-[{apikey.user}]-\n-[PRECIO BTC = {precio_btc:.2f}]-\n-[TOTAL USDT = {usdt + total_usdt_criptos:.2f}]-\n-[USDT = {usdt:.5f}]-\n-[ADA = {usdt_ada:.5f} - {ada:.5f}]-\n-[AGIX = {usdt_agix:.5f} - {agix:.5f}]-\n-[ALGO = {usdt_algo:.5f} - {algo:.5f}]-\n-[AVAX = {usdt_avax:.5f} - {avax:.5f}]-\n-[BTC = {usdt_btc:.5f} - {btc:.5f}]-\n-[DOT = {usdt_dot:.5f} - {dot:.5f}]-\n-[ETH = {usdt_eth:.5f} - {eth:.5f}]-\n-[FET = {usdt_fet:.5f} - {fet:.5f}]-\n-[FIL = {usdt_fil:.5f} - {fil:.5f}]-\n-[LINK = {usdt_link:.5f} - {link:.5f}]-\n-[LTC = {usdt_ltc:.5f} - {ltc:.5f}]-\n-[MATIC = {usdt_matic:.5f} - {matic:.5f}]-\n-[NEO = {usdt_neo:.5f} - {neo:.5f}]-\n-[RNDR = {usdt_rndr:.5f} - {rndr:.5f}]-\n-[RUNE = {usdt_rune:.5f} - {rune:.5f}]-\n-[SOL = {usdt_sol:.5f} - {sol:.5f}]-\n-[THETA = {usdt_theta:.5f} - {theta:.5f}]-\n-[WAVES = {usdt_waves:.5f} - {waves:.5f}]-\n-[XLM = {usdt_xlm:.5f} - {xlm:.5f}]-\n-[XRP = {usdt_xrp:.5f} - {xrp:.5f}]-\n-[UNI = {usdt_uni:.5f} - {uni:.5f}]-\n--------------------------------------------------\n')