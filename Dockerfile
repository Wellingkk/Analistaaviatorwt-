# Usa uma imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Comando para rodar sua aplicação
CMD ["python", "main.py"]
