FROM python:3.9-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia explicitamente o arquivo requirements
COPY requirements.txt .

# Instala as bibliotecas de forma forçada
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto
COPY . .

CMD ["python", "main.py"]
