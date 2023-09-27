# Prueba_Resuelve

1. A travez de la siguiente solucion de codigo por conola, se pretende que un bot haga una peticion HTTP get hacia la siguiente URL
https://stooq.com/q/l/?s={STOCK_CODE}.us&f=sd2t2ohlcv&h&e=csv, 
2. Guarda los datos en un Archivo CSV, del cual tambien los obtiene para verlos
3. Muestra una grafica con la fluctuacion de precios de la accion.
4. Eliminar entrada del historial de precios 

Para poder ejecutarse de debe de correr de modo local con python y atravez de consola 

## Instalación

Antes de ejecutar el Stock Bot, asegúrate de tener Python 3 instalado en tu sistema. Puedes descargar Python desde el sitio web oficial: [Python Downloads](https://www.python.org/downloads/).

Además, necesitas instalar algunas bibliotecas de Python. Abre tu terminal o línea de comandos y ejecuta el siguiente comando para instalar las dependencias:

```bash
pip install requests matplotlib
```
## Pruebas
Puedes ejecutar las pruebas usando el siguiente comando:

```bash
python -m unittest test 
