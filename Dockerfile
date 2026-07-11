FROM selenium/standalone-chrome:latest

USER root
WORKDIR /app

# Instala Python e dependências
RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Comando para rodar o bot
CMD ["python3", "main.py"]
