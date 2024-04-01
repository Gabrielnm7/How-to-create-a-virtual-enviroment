## Para crear un entorno virtual

En la terminal escribimos:
> virtualenv -p python3 venv

Se va a crear la carpeta env en la carpeta de trabajo que estes.
Recomendacion: No tocar nada de esa carpeta.

Para activarlo, (estando en la ruta de tu carpeta) vamos a escribir:
> .\env\Scripts\activate

Una ves que damos enter en la terminar va a aparecer algo asi:

Antes de darle click:
> PS C:\Users\usuario\Desktop\testing

Luego de darle click:

> (env) PS C:\Users\usuario\Desktop\testing

Dentro de este entorno voy a tener paquetes ya preinstalados, podemos verlo con el comando:

> pip list

y si queremos instalar alguno que vayamos a utilizar lo hacemos pip install (veamos como instalar pandas): 
> pip install pandas

## Vayamos a lo importante

Exportar los paquetes a un `.txt`. Para hacerlo escribimos en la consola el siguiente comando:

> pip freeze > requirements.txt 

Una vez que tenemos el requirements.txt, si alguna vez necesitamos que el entorno vuelva a instalar los paquetes por que usamos otra computadora, debemos ejecutar el siguiente comando dentro del `venv`

> pip install -r .\requirements.txt

Teniendo en cuenta que estamos escribiendo bien la ruta del archivo.

Para salir del entorno:

> deactivate