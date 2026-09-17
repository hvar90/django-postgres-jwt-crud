```markdown
# Django REST API CRUD + JWT + Docker

API REST desarrollada con **Django**, **Django REST Framework (DRF)**, **SimpleJWT** y **PostgreSQL**, completamente contenerizada con **Docker y Docker Compose**.

## 🚀 Requisitos previos

Asegúrate de tener instalado en tu equipo:
* [Docker](https://www.docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Instalación y Configuración Local

1. **Clona el repositorio o descarga el proyecto:**

   git clone https://github.com/hvar90/django-postgres-jwt-crud.git
   cd django-postgres-jwt-crud

```

2. **Crea el archivo de variables de entorno:**
Duplica el archivo de ejemplo `.env.example` y nómbralo `.env`:
```bash
cp .env.example .env

```


*(Los valores por defecto de `.env.example` ya están listos para funcionar con Docker).*

---

## 🏃‍♂️ Ejecución del Proyecto

1. **Levanta los contenedores con Docker Compose:**
```bash
docker-compose up --build

```


*(Esto iniciará la base de datos PostgreSQL y levantará el servidor de Django en `http://localhost:8000`).*
2. **Ejecuta las migraciones de la base de datos** (en una nueva pestaña de la terminal):
```bash
docker-compose exec web python manage.py migrate

```


3. **Crea un superusuario (opcional para verificar el panel de administración):**
```bash
docker-compose exec web python manage.py createsuperuser

```



---

## 🧪 Ejecución de Pruebas Unitarias

Para verificar que toda la lógica del CRUD y la autenticación JWT funcionan correctamente mediante las pruebas automatizadas de Django, ejecuta:

```bash
docker-compose exec web python manage.py test

```

---

## 📌 Endpoints Principales de la API

* **Obtener Token JWT (Login):** `POST /api/token/`
* **Body (JSON):**
```json
{"username": "tu_usuario", "password": "tu_password"}

```




* **Refrescar Token:** `POST /api/token/refresh/`
* **Body (JSON):**
```json
{"refresh": "tu_refresh_token"}

```




* **CRUD de Items** *(Requiere header: `Authorization: Bearer <tu_access_token>`)*:
* **Listar / Crear:** `GET /api/items/` | `POST /api/items/`
* **Ver / Actualizar / Borrar:** `GET /api/items/{id}/` | `PUT /api/items/{id}/` | `DELETE /api/items/{id}/`



```

```