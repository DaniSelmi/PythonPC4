import requests

def obtener_precio_bitcoin():
    try:
        # Realizar la solicitud a la API de CoinDesk
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()  # Detecta errores HTTP
        datos = respuesta.json()
        
        # Extraer el precio actual del Bitcoin en USD
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Ocurrió un error al intentar obtener el precio de Bitcoin:", e)
        return None

def calcular_valor_bitcoins(n, precio_usd):
    # Calcular el valor total de n Bitcoins en USD
    return n * precio_usd

def main():
    # Solicitar al usuario el número de Bitcoins que posee
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Obtener el precio actual del Bitcoin en USD
    precio_usd = obtener_precio_bitcoin()
    if precio_usd is None:
        return

 # Calcular y mostrar el costo actual de "n" Bitcoins en USD
    valor_total = calcular_valor_bitcoins(n, precio_usd)
    print(f"El costo actual de {n} Bitcoins es: ${valor_total:,.4f}")

if __name__ == "__main__":
    main()