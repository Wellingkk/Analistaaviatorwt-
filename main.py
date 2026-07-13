import cloudscraper
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8952208320:AAFRmo8v5xk7GlnPm8qTd7WzQQPAnE2Y6QI"
CHAT_ID = "5805588750"

bot = telebot.TeleBot(TOKEN)

# Servidor para manter o Render online
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

# Vamos tentar acessar uma rota comum de API que esses sites usam
# Muitas vezes os sinais ficam em /api/signals ou /api/data
URL_API = "https://sorte.blackaviator.app/api/signals"

print("🚀 Buscando sinais na API...")

while True:
    try:
        response = scraper.get(URL_API, timeout=10)
        if response.status_code == 200:
            bot.send_message(CHAT_ID, f"🔍 API respondeu: {response.text[:500]}")
        else:
            bot.send_message(CHAT_ID, f"⚠️ A página principal carrega, mas a API retornou erro: {response.status_code}")
    except Exception as e:
        bot.send_message(CHAT_ID, f"❌ Erro na busca: {str(e)[:50]}")
    
    time.sleep(60)
