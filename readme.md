# Prueba técnica para Claro shop

La prueba técnica consiste en un api muy sencillo en el cual se define un solo endpoint con dos funcionalidades basadas en los parámetros de la petición.

La funcionalidad principal se localiza en el archivo **app/prueba.py**, ahí está codificada la función que consume el servicio de pokeapi y regresa el payload al cliente.

De igual manera el proyecto cuenta con un archivo de constantes **utils/constants.py** en caso de que hubiera una actualización en el url de pokeapi solamente sería necesario actualizar este archivo.

El proyecto cuenta también con pruebas unitarias implementadas las cuales se localizan en el archivo **tests/test_pokemon_endpoint.py** se pueden correr desde una consola.

Así mismo el código cumple con los siguientes estándares de estilo para asegurar que sea limpio y escalable:

- PEP8
- PyFlake
- McCabe complexity

Esta revisión se hace con la librería **flake8**

## Documentación del endpoint

### /api/pokemon

- Verbos aceptados: **Get**
- query params:
	- limit:
		- Descripción: Número de elementos que queremos regresar en la respuesta del servicio
		- Tipo de dato: entero
	- offset:
		- Descripción: Número de id a partir del cual se regresara
		- Tipo de dato: entero

#### Descripción
Este servicio paginado regresa una lista con una longitud default de 20 elementos con el id y el nombre de pokemones.

Así mismo regresa el conteo total de los pokemones registrados hasta el momento y al ser un servicio paginado también regresa las ligas para los conjuntos siguientes y anteriores a los que estamos solicitando.

#### Respuesta

```
{
  "control": {
    "anterior": null,
    "siguiente": "http://127.0.0.1:5000/pokemon?offset=5&limit=5"
  },
  "resultados": [
    {
      "id": 1,
      "nombre": "bulbasaur"
    },
    {
      "id": 2,
      "nombre": "ivysaur"
    },
    {
      "id": 3,
      "nombre": "venusaur"
    },
    {
      "id": 4,
      "nombre": "charmander"
    },
    {
      "id": 5,
      "nombre": "charmeleon"
    }
  ],
  "total": 1302
}
```

### /api/pokemon/<pokemon_id>

- Verbos aceptados: **Get**
- Parámetros:
	- pokemon_id:
		- Descripción: Id del pokemon del cual queramos la información
		- tipo de dato: Entero

#### Descripción
Este servicio regresa la información detallada del pokemon definido.

#### Posibles respuestas

##### 200
En caso de que el pokemon id sea válido, recibiremos un json con la info del pokemon

```
{
  "abilities": [
    {
      "ability": {
        "name": "blaze",
        "url": "https://pokeapi.co/api/v2/ability/66/"
      },
      "is_hidden": false,
      "slot": 1
    },
    {
      "ability": {
        "name": "solar-power",
        "url": "https://pokeapi.co/api/v2/ability/94/"
      },
      "is_hidden": true,
      "slot": 3
    }
  ],
  "base_experience": 62,
  "cries": {
    "latest": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/4.ogg",
    "legacy": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/4.ogg"
  },
  "forms": [
    {
      "name": "charmander",
      "url": "https://pokeapi.co/api/v2/pokemon-form/4/"
    }
  ],
  "game_indices": [
    {
      "game_index": 176,
      "version": {
        "name": "red",
        "url": "https://pokeapi.co/api/v2/version/1/"
      }
    },
    {
      "game_index": 176,
      "version": {
        "name": "blue",
        "url": "https://pokeapi.co/api/v2/version/2/"
      }
    },
    ...
  ]
  ...
}
```

#### 404
En caso que el id sea inválido, el servicio regresará un 404

```
Not Found

Pokemon no encontrado
```

## Manual de implementación

### Requisitos

- Consola con Python 3.12
- git (en caso de querer clonar el proyecto)
- el paquete de python **venv**
	- en caso de no estar instalado se puede instalar de manera global con los comandos:
		- `sudo apt-get update`
		- `sudo apt-get install python3-virtualenv`
- De preferencia utilizar wsl o un ambiente linux

## Descompresión del zip o clonado del repositorio
Para obtener el código fuente se puede descargar el archivo zip adjunto en el correo o bien a través del repositorio público: https://github.com/MisaStrikesBack/claro_test.git

En caso de clonar el archivo, nos colocamos en la carpeta en la que queramos clonar el proyecto y escribimos el siguiente comando en la consola.

`git clone https://github.com/MisaStrikesBack/claro_test.git`

## Creación del ambiente virtual
Una vez que tengamos el código del proyecto tenemos que crear un ambiente virtual para encapsular las dependencias.

Desde el directorio raíz del proyecto, primero se debe inicializar el ambiente virtual.

Si seguimos en el 

para esto escribimos el comando:

`python3 -m venv venv`

## Instalación de dependencias
para instalar las dependencias utilizamos pip y el archivo requirements.txt donde están listadas todas las dependencias del proyecto.
En la consola escribimos:
`pip install -r requirements.txt`

## Arrancando el servidor de desarrollo
Para arrancar el proyecto utilizamos el servidor de desarrollo de flask

`flask --app app.prueba --debug run`

Esto iniciará un servidor de pruebas con el cual podremos realizar peticiónes al url:

`http://127.0.0.1:5000/api/pokemon`
`http://127.0.0.1:5000/api/pokemon/<pokemon_id`


## Corriendo las pruebas unitarias
Para correr las pruebas unitaras utilizamos el comando de pytest en la consola.

Para correr las pruebas unitarias **También debe estar activado el ambiente virtual**

En caso de que no esté activado el ambiente virtual, lo activamos con el comando:

`source venv/bin/activate`

Una vez que el ambiente virtual está activo procedemos a correr las pruebas con el comando:

`pytest`


## Contacto
Cualquier duda o comentario al respecto del código se puede contactar al desarrollador en el correo **misael@casagris.dev**
