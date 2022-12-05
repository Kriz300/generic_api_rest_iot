# API IoT
Proyecto integrando una API REST con Flask y una Base de datos SQLite.
## Ejecución y Comandos 🔧

La ejecución es bien simple y directa, solo se debe descargar el repo, entrar en la caperta generada donde se encuentra el archivo app.py, donde se debe ejecutar uno de los siguientes comandos dependiendo de su instalación de Python. La API esta diseñada en Python 3.

```
python3 -m flask run --port [portnumber]

python -m flask run --port [portnumber]

py -m flask run --port [portnumber]
```

Para realizar consultas a la API se deben utilizar las siguientes rutas:

```
#Consulta GET
https://[sitio/ip]:[portnumber]/api/v1/[tarjet]/?key=[company_api_key]

https://[sitio/ip]:[portnumber]/api/v1/sensor_data/?from=[EPOCH_time]&to=[EPOCH_time]&key=[sensor_api_key]&id=[sensor_id]


#Editar PUT
https://[sitio/ip]:[portnumber]/api/v1/[tarjet]/?id=[company_api_key]

#Insertar datos POST
https://[sitio/ip]:[portnumber]/api/v1/[tarjet]/

#Eliminar datos Datos
https://[sitio/ip]:[portnumber]/api/v1/[tarjet]/
```
Los parametros que aparecen en los comandos se explican a continuación:

* Sitio / IP: Corresponde a la url del servidor donde se aloja la API.
* PortNumber: Corresponde al puerto donde esta o se desea ejecutar la API.
* Tarjet: Corresponde al elemento que se desea consultar, por ejemplo company, location, etc.
* company_api_key y sensor_api_key: Corresponden a un identificador del elemento almacenado en la tabla correspondiente.
* EPOCH_time: Es un numero que al interpretarse corresponde a fecha y hora.


## Estructura 🛠️

### Construido con:

* **Python**
* **Flask**
* **SQLite**



## Autores ✒️

* **Christian Muñoz I.** [Kriz](https://github.com/Kriz300)
* **Camilo Rubilar** [Niyet](https://github.com/niyetsin)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.