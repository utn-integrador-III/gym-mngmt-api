# Docker - Gym Management API (FastAPI)

Guía rápida para levantar el backend de Gym Management con Docker Compose.

## Requisitos

- Docker y Docker Compose instalados
- Puertos disponibles:
  - API: 8000
  - MongoDB: 27017

## Archivos relevantes

- `Dockerfile`: build de la imagen de la API (FastAPI + Uvicorn)
- `docker-compose.yml`: orquesta API y MongoDB para desarrollo

## Variables de entorno clave

- `APP_PORT` (default: 8000): puerto interno de la API
- `MONGO_URI` (default: `mongodb://mongo:27017/`): cadena de conexión que consume `app/config/mongo.py`
  - La base de datos por defecto está definida en código: `gym_management_db`

## Comandos básicos

Ejecutar todos los comandos desde esta carpeta: `gym-mngmt-api-dev/Docker/`

- Construir y levantar en modo desarrollo (hot reload):

```bash
# build + up
docker compose up --build

# en segundo plano
# docker compose up --build -d
```

- Ver logs:

```bash
docker compose logs -f backend
```

- Probar la API (Swagger):

- http://localhost:8000/docs

- Detener contenedores:

```bash
docker compose down
```

- Limpiar volúmenes (elimina datos de Mongo locales):

```bash
docker compose down -v
```

## Nombres de imagen y contenedores

Se definen en `docker-compose.yml`:

- API
  - `image: myorg/gym-api:dev`
  - `container_name: gym-api-dev`
- MongoDB
  - `container_name: gym-mongo-dev`

Si prefieres evitar `container_name`, puedes usar un prefijo de proyecto:

```bash
docker compose -p gymapi up -d
```

## Cambiar puertos

- Puerto expuesto de la API: edita en `docker-compose.yml` la sección `ports`:

```yaml
services:
  backend:
    environment:
      - APP_PORT=8000
    ports:
      - "8000:8000"  # host:container
```

- Si cambias `APP_PORT`, asegúrate de reflejar el cambio en el mapeo `ports`.

## Usar MongoDB Atlas en vez de contenedor local

1) Cambia `MONGO_URI` en `docker-compose.yml` a tu cadena de conexión Atlas:

```yaml
environment:
  - MONGO_URI=mongodb+srv://<user>:<pass>@<cluster>/?retryWrites=true&w=majority
```

2) Opcional: comenta o elimina el servicio `mongo` y la sección `volumes`.

## Notas y solución de problemas

- Advertencia `version is obsolete`: puedes eliminar la línea `version: "3.8"` del compose si quieres silenciarla. No bloquea el uso.
- Errores de instalación `pip`: este Dockerfile limpia líneas no válidas del `requirements.txt` en tiempo de build. Si agregas dependencias nuevas, asegúrate de que cada línea contenga solo `paquete==version` (sin comandos ni comentarios en la misma línea).
- CORS: la API está configurada para permitir `http://localhost:3000` por defecto en `app/main.py`. Si tu frontend corre en otro puerto (p. ej. 5173), agrega ese origen.

## Estructura del contenedor

- API corre con Uvicorn y `--reload` (solo desarrollo)
- El código del host se monta en `/usr/src/app` para hot reload:

```yaml
volumes:
  - ..:/usr/src/app
```

Para producción: quita `--reload`, el bind mount, y usa una imagen con tag específico.
