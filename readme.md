## Para crear un entorno virtual

En la terminal escribimos:

```bash
virtualenv -p python3 venv
```

Si nos llega a aparecer un error es por que no tenemos instalado el paquete de virtualenv en nuestra computadora local. Para instalarlo ejecutamos en la terminal:

``` bash
pip install virtualenv
```

Luego ejecutamos el comando anterior y se va a crear la carpeta venv en la carpeta de trabajo que tengas abierta en tu IDE de preferencia.

**_Recomendacion_**: No tocar nada de esa carpeta.

Para activarlo, (estando en la ruta de tu carpeta) vamos a escribir:
> .\venv\Scripts\activate

## `Nota` si nos sale un error como:
+ No se puede cargar el archivo C:\Users\Usuario\Desktop\testing\venv\Scripts\activate.ps1 porque la ejecución de scripts está deshabilitada en este sistema...

El error que estás viendo se debe a que la política de ejecución de PowerShell en tu sistema está configurada para no permitir la ejecución de scripts, que es una medida de seguridad.

Para solucionar este problema, puedes cambiar temporalmente la política de ejecución para permitir la ejecución de scripts. Aquí te muestro cómo hacerlo:

Abre PowerShell como administrador.
Ejecuta el siguiente comando:

> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser


Por razones de seguridad, es posible que desees volver a establecer la política de ejecución a su valor original después de activar tu entorno virtual. Puedes hacerlo con el siguiente comando:
> Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser


## Una ves que damos enter en la terminal para activar el entorno va a aparecer algo asi:

Antes de darle `click`:
> PS C:\Users\usuario\Desktop\testing

Luego de darle `click`:

> (env) PS C:\Users\usuario\Desktop\testing

Dentro de este entorno vas a tener paquetes ya preinstalados, podemos verlo con el comando:

> pip list

y si queremos instalar alguno que vayamos a utilizar lo hacemos pip install (veamos como instalar pandas): 
> pip install pandas

## Vayamos a lo importante

Exportar los paquetes a un `.txt`. Para hacerlo escribimos en la consola el siguiente comando:

> pip freeze > requirements.txt 

Una vez que tenemos el requirements.txt, si alguna vez necesitamos que el entorno vuelva a instalar los paquetes por que usamos otra computadora, debemos ejecutar el siguiente comando dentro del `venv`

> pip install -r .\requirements.txt

Teniendo en cuenta que estamos escribiendo bien ***la ruta del archivo***.

Para salir del entorno solo ejecutamos el siguiente codigo en la terminal:

> deactivate