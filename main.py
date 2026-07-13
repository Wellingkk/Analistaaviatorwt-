import cloudscraper
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

# Suas credenciais
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

# Configuração com o novo link
scraper = cloudscraper.create_scraper()
URL = "https://sorte.blackaviator.app/"

print("🚀 Bot iniciado com o link da Black Aviator!")

while True:
    try:
        response = scraper.get(URL, timeout=15)
        
        if response.status_code == 200:
            bot.send_message(CHAT_ID, "✅ Sucesso! O bot conseguiu acessar o site blackaviator.app sem erro 403!")
        else:
            bot.send_message(CHAT_ID, f"❌ Erro ao acessar: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        bot.send_message(CHAT_ID, f"❌ Erro na conexão: {str(e)[:50]}")
    
    # Pausa de 60 segundos antes de tentar de novo
    time.sleep(60)
