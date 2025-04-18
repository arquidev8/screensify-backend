FROM python:3.10-slim
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

# Exponer puerto
EXPOSE 8000

# Arrancar migraciones y servidor
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
