FROM python:3.11-slim

WORKDIR /app

# Instala dependencias del sistema y psycopg2 requiere gcc y libpq-dev
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia la app y el script de espera
COPY app ./app
COPY wait_db.py ./wait_db.py

# CMD final: espera a la DB y luego arranca Uvicorn
CMD ["sh", "-c", "python wait_db.py && uvicorn app.main:app --host 0.0.0.0 --reload"]