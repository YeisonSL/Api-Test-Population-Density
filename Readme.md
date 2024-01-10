
# Api Test Population Density

## ⚙️ Descripción ⚙️

El siguiente proyecto basado en Python es par la creación de una api, que retorna la información de los 5 paises de mundo con mayor densida demografica.

## 📦 Pre-requisitos 📦

1) Instalar python https://www.python.org/downloads/

2) crear un ambiente en python ejecutando en consola: 
    python -m venv venv

3) habilitar el ambiente virtual ejecutando en consola:
    .\venv\Scripts\activate

4) instalar las dependencias ejecutando en consola:
    python -m pip install -r .\requirements.txt
    

## 🛠️ Levantar API 🛠️

Para poner en marcha nuestra API, basta con ejecutar ejecutar nuestra app, para ello ejecutamos en consola el siguiente comando:
    uvicorn api.operation.get_API:app --reload

 Por ultimo ingresamos a la url: http://localhost:8000/densidad-demografica para la validación que nuestra API responde

 ## ⚙️ Pruebas Unitarias ⚙️

Para ejecutar nuentras pruebas unitarias basta ejecutar en consola el comnado ** pytest -v **

