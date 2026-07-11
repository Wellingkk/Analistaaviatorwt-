FROM python:3.10-slim

WORKDIR /app

# Instala apenas as bibliotecas básicas
RUN pip install --no-cache-dir requests python-telegram-bot

COPY main.py .

CMD ["python", "-u", "main.py"]
