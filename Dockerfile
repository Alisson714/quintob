# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias y código
COPY app.py requirements.txt /app/

# Instalar Flask
RUN pip install -r requirements.txt

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Comando por defecto
CMD ["python", "app.py"]

