

# Imagen base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install virtualenv
RUN pip install virtualenv

# Create virtual environment
RUN virtualenv venv

# Activate virtual environment 
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install streamlit

# Copiar el resto del código
COPY . .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=3.86.189.113"]