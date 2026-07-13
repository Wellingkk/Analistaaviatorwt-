import cloudscraper
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8952208320:AAFRmo8v5xk7GlnPm8qTd7WzQQPAnE2Y6QI"
CHAT_ID = "5805588750"

bot = telebot.TeleBot(TOKEN)

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

# Configuração do scraper que simula um navegador real
scraper = cloudscraper.create_scraper()
URL = "https://tipminer.com/aviator"

print("🚀 Bot iniciado com Cloudscraper!")

while True:
    try:
        response = scraper.get(URL, timeout=15)
        if response.status_code == 200:
            bot.send_message(CHAT_ID, "✅ Site acessado com sucesso via Cloudscraper!")
        else:
            bot.send_message(CHAT_ID, f"❌ Erro ao acessar: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
        bot.send_message(CHAT_ID, f"❌ Erro no bot: {str(e)[:50]}")
    
    time.sleep(60)
