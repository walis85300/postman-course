# Curso de Postman Platzi

## Protocolo HTTP
Un protocolo especifica reglas en la comunicacion entre dos entes, en este caso entre dos computudoras.

HTTP (Hyper Text Transfer Protocol) fue creado especificamente para la web.

----------

### Verbos 
- **GET**: solicitar datos o algun recurso.
- **HEAD**: traer headers (como una peticion GET pero sin contenidos). Es util cuando vamos a utilizar APIs, para comprobar si lo que vamos a enviar esta correcto y puede ser procesado.
- **POST**: enviar datos a un recurso para la creación.
- **PUT**: reemplazar por completo un recurso.
- **PATCH**: reemplazar parcialmente un recurso.
- **DELETE**: eliminar un recurso.

----------

### Codigos de Estados
- **1xx**: Indican que la peticion fue recibida y el servidor sigue trabajando en el proceso, es decir, no fue exitosa ni fue errónea, sino que esta siendo procesada aun.
- **2xx**: Indican que la peticion fue recibida y procesada correctamente.
- **3xx**: Indican que hay que tomar acciones adicionales para completar la solicitud. Por lo general estos codigos indican redireccion. Generalmente en los APIs no se usan redirecciones porque no contienen estados, es decir, toda la informacion esta contenida en una solicitud, no se guarda un estado en el servidor con una sesion por ejemplo.
- **4xx**: Indican errores del lado del cliente, por ejemplo: se hizo mal la solicitud, faltan datos, headers o cualquier otro error que pueda ocurrir.
- **5xx**: Indican errores del servidor. Suelen aparecer cuando existe un fallo en la ejecución en el servidor.

----------
### Codigos mas comunes
- **200**: Todo esta OK.
- **201**: Todo OK cuando se hizo una solicitud POST, el recurso se creo y se guardo correctamente.
- **204**: Indica que la solicitud se completo correctamente pero no devolvio informacion. Es muy comun cuando se hacen peticiones con el verbo DELETE.
- **400**: Bad Request, algo esta mal en la peticion. Se nos olvido enviar un dato o algo relacionado. Por lo general la respuesta nos especifica cuales fueron los errores a la hora de hacer la peticion.
- **401**: Unauthorized, es decir, no estamos autorizados (autenticados) a realizar la peticion.
- **403**: Forbidden, yo no tengo acceso a ese recurso aunque este autenticado.
- **404**: Not Found, no existe el recurso que se esta intentando acceder.
- **500**: Interna Server Error, es un error que retorna el servidor cuando la solicitud no pudo ser procesada. Por lo general, si no tenemos acceso al backend, no tenemos control sobre los errores 500 que retorna un API.
----------


# This is the API for Postman Course

It is a simple version of an API builded with Django and Django Rest Framework
using Docker.


# You can learn how to build APIs here:

- [Curso de API REST](https://platzi.com/clases/api-rest/)
- [Curso de Django](https://platzi.com/clases/django/)
- [Curso Avanzado de Django](https://platzi.com/clases/django-avanzado/)
- [Curso de Fundamentos de Docker](https://platzi.com/clases/docker/)

# How to run this project
- Install Docker and Docker Compose
- Execute `docker-compose up -d`: This command starts a local server with the API running over 8000 port.
- Get inside the docker container executing `docker exec -it postman-course_web_1 bash`
- Exec `cd ./project`
- Run migrations `python manage.py migrate`
- Inside the docker container execute `source admin_info.sh`
- Load initial data from fixture: `python manage.py loaddata courses/fixtures/initial_data.json`

# How to use it
Once the development server is running you can access to the [Django Admin](http://localhost:8000/admin/), there you can perform CRUD operations over the resources. 


# What can you do with it?
## ANYTHING YOU WANT 

This code is free, use it, change it, even you can send me pull requests. Maybe a pull requests with some fixtures of Courses and Materials.


## API Update: April 13, 2020

- Created fixture: now you have initial data for testing. Some courses, materials, teachers and videos are created in this fixture.
- Updated folder for execute server: now is mandatory access to `project` folder for execute the development server.
- Public APIs for testing: some of you have had some issues running this project, I can give you some public APIs that some students have left in contributions (remember this course is a Postman course not and API Creation Course)
    - [Rick & Morty API](https://rickandmortyapi.com/api/character/)
    - [Repository with Public APIs](https://github.com/public-apis/public-apis)

- Make `git pull` and follow [the steps](https://github.com/walis85300/postman-course#how-to-run-this-project)
