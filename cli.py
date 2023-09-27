import requests
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Buscar la accion y regresa su valor
# parametro 
# 'stock_code' : Es el codigo por el cual se identifica la accion, Ejemplo: AAPL 
#  
def consultar_precio(stock_code):
    url = f'https://stooq.com/q/l/?s={stock_code}.us&f=sd2t2ohlcv&h&e=csv'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        #print ("El de data es: "+data)
        filas = data.split('\n')
        #print ("El de filas es: "+filas[1])
        if len(filas) > 1:
            col = filas[1].split(',')
            if len(col) > 1:
                #print ("El valor es: "+ col[6])
                return col[6]  # El precio se encuentra en la sexta columna
    return None

# Dentro del CSV se guarda el nombre de la accion y el precio
# parametros:
#  'stock_code' : Es el codigo por el cual se identifica la accion, Ejemplo: AAPL 
#  'precio' : El valor el cual tiene la accion  
def guardar_precio(stock_code, price):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('historial.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([stock_code, price, fecha_actual])

# Eliminar una entrada del historial de precios
def eliminar_entrada_historial():
    if not os.path.exists('historial.csv'):
        print("Aún no hay historial, primero intenta buscar una acción")
        return

    print("Historial de precios:")
    mostrar_historial()

    entrada_a_eliminar = input("Ingrese el código de la acción que desea eliminar del historial: ")

    # Leer el historial y crear una lista de entradas excluyendo la entrada a eliminar
    nuevas_entradas = []
    with open('historial.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != entrada_a_eliminar:
                nuevas_entradas.append(row)

    # Sobrescribir el historial con las nuevas entradas
    with open('historial.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for entrada in nuevas_entradas:
            writer.writerow(entrada)

    print(f"La entrada para {entrada_a_eliminar} ha sido eliminada del historial de precios.")


# Obtener el historial de precios guardados en el CSV
def mostrar_historial():
    if not os.path.exists('historial.csv'):
        print("Aún no hay historial, primero intenta buscar una accion")
        return

    with open('historial.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'{row[0]}: {row[1]}')

# Graficar la variacion del precio de acciones
def mostrar_grafico():
    if not os.path.exists('historial.csv'):
        print("No se encontraron datos en el historial para generar gráficos.")
        return

    # Obtener la lista de códigos de acciones únicos del historial
    stock_codes = set()
    with open('historial.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            stock_codes.add(row[0])

    # Generar y mostrar un gráfico para cada acción en el historial
    for stock_code in stock_codes:
        stock_prices = []
        dates = []
        with open('historial.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == stock_code:
                    stock_prices.append(float(row[1]))
                    dates.append(row[2])

        plt.figure(figsize=(10, 6))
        plt.plot(dates, stock_prices)
        plt.xlabel('Fechas')
        plt.ylabel('Precios')
        plt.title(f'Variación de Precios de {stock_code}')
        plt.xticks(rotation=45)
        plt.show()

# Función principal del bot
def main():
    while True:
        print("\nOpciones:")
        print("1. Consultar precio de una acción")
        print("2. Mostrar historial de precios")
        print("3. Mostrar gráfico de variación de precios")
        print("4. Eliminar entrada del historial de precios")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            stock_code = input("Ingrese el código de la acción (por ejemplo, AAPL): ")
            precio = consultar_precio(stock_code)
            if precio != "N/D":
                print(f'El precio de {stock_code} es: ${precio}')
                guardar_precio(stock_code, precio)
            else:
                print(f'No se pudo obtener el precio de {stock_code}.')

        elif opcion == '2':
            mostrar_historial()

        elif opcion == '3':
            mostrar_grafico()

        elif opcion == '4':
            eliminar_entrada_historial()

        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
