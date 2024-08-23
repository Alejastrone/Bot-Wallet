from datetime import datetime
from binance.client import Client
import apikey
import tkinter as tk

# Inicializar el cliente
client = Client(apikey.API_KEY, apikey.API_SECRET, tld='com')

# Obtener el balance de la cuenta
balanceCripto = client.get_account()

# Lista de activos
activos = ["AAVE","ADA", "ALGO", "ATOM", "AVAX", "BTC", "DOT", "ETH", "FET", "FIL", "INJ", "LINK", "LTC", "MATIC", "MKR", "NEO", "RUNE", "SOL", "TAO", "THETA", "XLM", "XRP"]
# Inicializar un diccionario para almacenar el valor en USDT de cada activo
valores_usdt = {}
balances = {b['asset']: float(b['free']) for b in balanceCripto['balances']}

# Función para calcular el valor en USDT
def calcular_valor_usdt(activo):
    balance = balances.get(activo, 0.0)
    precio = client.get_avg_price(symbol=f'{activo}USDT')['price']
    return balance * float(precio)

# Calcular valores en USDT para cada activo
for activo in activos:
    valores_usdt[activo] = calcular_valor_usdt(activo)

# Calcular el total en USDT
total_usdt_criptos = sum(valores_usdt.values())

# Obtener el balance en USDT
usdt = balances.get("USDT", 0.0)

# Imprimir los resultados
for activo, valor in valores_usdt.items():
    print(f"{activo} = {balances.get(activo, 0.0):.5f}")
    print(f"USDT {activo.lower()} = {valor:.2f}")

print(f"\nUSDT = {usdt:.2f}")
print(f"Total USDT en criptos = {total_usdt_criptos:.2f}")
print(f"Total de USDT = {usdt + total_usdt_criptos:.2f}")

# Función para escribir en el archivo
def escribir_archivo():
    date = datetime.now()
    year = date.strftime('%m %Y')
    fecha = date.strftime('%d %m')
    hour = date.strftime("%H:%M")
    
    with open(f"Cartera {apikey.user} {year}.txt", "a") as f:
        f.write(f'Fecha: {fecha}\nHora: {hour}\nUser: {apikey.user}\n')
        for activo in activos:
            f.write(f'{activo}: {valores_usdt[activo]:.2f}\n')
        f.write(f'USDT: {usdt:.2f}\n')
        f.write(f'Total: {usdt + total_usdt_criptos:.2f}\n')
        f.write(f'PnL: {((usdt + total_usdt_criptos) - 3850):.2f}\n')
        f.write('--------------------------------------------------\n')

# Función para mostrar el mensaje en una ventana
def show_message():
    date = datetime.now()
    fecha = date.strftime('%d %m')
    hour = date.strftime("%H:%M")
    
    letrero = (f"Fecha: {fecha}\n-------------------\n"
               f"Criptos: {total_usdt_criptos:.2f}\n"
               f"Dólares: {usdt:.2f}\n"
               f"Total: {usdt + total_usdt_criptos:.2f}\n"
               f"PnL: {((usdt + total_usdt_criptos) - 3850):.2f}\n"
               f"-------------------\nHora: {hour}")

    root = tk.Tk()
    root.title(f"Cartera {apikey.user}")

    label = tk.Label(root, text=letrero)
    label.pack(padx=50, pady=50)

    root.after(45000, root.destroy)
    root.mainloop()

# Ejecutar las funciones
escribir_archivo()
show_message()