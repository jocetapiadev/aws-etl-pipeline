FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecuta el script del pipeline al iniciar el contenedor
CMD ["python", "etl_pipeline.py"]
