FROM python:3.12-alpine

# Dependencias de sistema para paquetes como cryptography/bcrypt/motor
RUN apk add --no-cache build-base libffi-dev openssl-dev python3-dev musl-dev

WORKDIR /usr/src/app

# Instalar dependencias de Python
COPY requirements.txt .
# Limpiar líneas no válidas de requirements.txt (e.g., '--privada', 'pip install ...', y líneas con espacios como comandos)
RUN awk 'BEGIN{IGNORECASE=1} !/^\s*#/ && !/^\s*--/ && !/^\s*pip\s+install/ && $0 !~ /\s/ && $0 !~ /^\s*$/' requirements.txt > requirements.clean
RUN pip install --no-cache-dir -r requirements.clean

# Copiar el resto del código
COPY . .

# Puerto por defecto (se puede sobreescribir por variable de entorno)
ENV APP_PORT=8000

# Ejecutar FastAPI con Uvicorn (hot reload para desarrollo)
CMD uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT:-8000} --reload