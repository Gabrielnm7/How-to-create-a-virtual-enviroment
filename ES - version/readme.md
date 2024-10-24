<h1 align="center"> Tutorial basico de como crear un entorno virtual </h1>

### Para version en ingles, [click aca](../)

### Configuración del Entorno Virtual

Para crear un entorno virtual, primero asegurate de estar en el directorio donde querés que se cree el entorno. Luego, ejecutá el siguiente comando en la terminal:

```bash
python -m venv ejemplo-venv
```

Este comando generará una carpeta llamada `ejemplo-venv` en el directorio de trabajo actual y utilizará la versión actual de Python que tengas instalada. Podés verificar qué versión de Python estás usando con el siguiente comando:

```bash
python --version
```

> [!TIP]
> 1. Una ruta común para el directorio del entorno virtual es `venv` (abreviatura de **V**irtual **ENV**ironment).
> 2. No modifiques nada dentro de esta carpeta.

Para activarlo, (estando en la ruta de tu carpeta) vamos a escribir:
> .\ejemplo-venv\Scripts\activate

## `Nota` si nos sale un error como:
> No se puede cargar el archivo C:\Users\Usuario\Desktop\testing\venv\Scripts\activate.ps1 porque la ejecución de scripts está deshabilitada en este sistema...

El error que estás viendo se debe a que la política de ejecución de PowerShell en tu sistema está configurada para no permitir la ejecución de scripts, que es una medida de seguridad.

Para solucionar este problema, puedes cambiar temporalmente la política de ejecución para permitir la ejecución de scripts. Aquí te muestro cómo hacerlo:

Abre PowerShell como administrador.
Ejecuta el siguiente comando:

```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

Por razones de seguridad, es posible que desees volver a establecer la política de ejecución a su valor original después de activar tu entorno virtual. Puedes hacerlo con el siguiente comando:
```bash
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser
```


## Una ves que damos enter en la terminal (para activar el entorno) va a aparecer algo asi:

Antes de darle `enter`:
> PS C:\Users\usuario\Desktop\testing

Luego de darle `enter`:

> (env) PS C:\Users\usuario\Desktop\testing

**Dentro** de este entorno vas a tener paquetes ya preinstalados, podemos verlo con el comando:

```bash
pip list
```

y si queremos instalar alguno que vayamos a utilizar lo hacemos utilizando el comando pip install (veamos como instalar pandas): 
```bash
pip install pandas
```
## Vayamos a lo **importante**

Exportar los paquetes a un `.txt`. Para hacerlo escribimos en la consola el siguiente comando:

```bash
pip freeze > requirements.txt 
``` 

Una vez que tenemos el requirements.txt, si alguna vez necesitamos que el entorno vuelva a instalar los paquetes por que usamos otra computadora, debemos ejecutar el siguiente comando dentro del `venv`

```bash
pip install -r .\requirements.txt
```
Teniendo en cuenta que estamos escribiendo bien ***la ruta del archivo del requirements.txt***.

Para salir del entorno solo ejecutamos el siguiente codigo en la terminal:

```bash
deactivate
```