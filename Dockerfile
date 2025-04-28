

# Imagen base
FROM python:3.12-slim


# Carpeta de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt


# Copiar el resto del código
COPY . .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=3.86.189.113"]