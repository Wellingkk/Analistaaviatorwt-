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

scraper = cloudscraper.create_scraper()
URL = "https://sorte.blackaviator.app/"

print("🚀 Bot iniciado!")

while True:
    try:
        response = scraper.get(URL, timeout=15)
        if response.status_code == 200:
            # Pega os primeiros 800 caracteres para eu analisar a estrutura
            conteudo = response.text[:800]
            bot.send_message(CHAT_ID, f"🔍 Conteúdo recebido:\n\n{conteudo}")
        else:
            bot.send_message(CHAT_ID, f"❌ Erro: {response.status_code}")
    except Exception as e:
        bot.send_message(CHAT_ID, f"❌ Erro: {str(e)[:50]}")
    
    time.sleep(60)
