import cloudscraper
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8952208320:AAFRmo8v5xk7GlnPm8qTd7WzQQPAnE2Y6QI"
CHAT_ID = "5805588750"

bot = telebot.TeleBot(TOKEN)

# Mantém o Render acordado
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

scraper = cloudscraper.create_scraper()
URL = "https://sorte.blackaviator.app/"

print("🚀 Bot iniciado em modo de varredura profunda...")

while True:
    try:
        # Acessa a página principal
        response = scraper.get(URL, timeout=15)
        
        # Procura por palavras-chave comuns em sinais
        if "entrada" in response.text.lower() or "sinal" in response.text.lower() or "confirmado" in response.text.lower():
            bot.send_message(CHAT_ID, "✅ SINAL DETECTADO! O conteúdo contém palavras de entrada.")
        else:
            # Envia um pedaço maior do conteúdo para eu ver se os dados aparecem em JSON escondido
            bot.send_message(CHAT_ID, f"🔍 Varredura: {response.text[2000:2500]}")
            
    except Exception as e:
        print(f"Erro: {e}")
    
    time.sleep(120)
