FROM python:3.10-slim

# Instala dependências do sistema e o Chromium estável para o Selenium rodar
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxrender1 \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Configura as variáveis de ambiente para o Selenium achar o navegador no servidor
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromium-driver

WORKDIR /app

# Instala as bibliotecas que o seu robô usa
RUN pip install --no-cache-dir selenium requests

COPY main.py .

CMD ["python", "-u", "main.py"]
