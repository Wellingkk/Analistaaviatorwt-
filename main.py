import requests
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configurações do Bot
TOKEN = "8952208320:AAFRmo8v5xk7GlnPm8qTd7WzQQPAnE2Y6QI"
CHAT_ID = "5805588750"  # Seu ID pessoal

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

URL = "https://tipminer.com/aviator"
headers = {"User-Agent": "Mozilla/5.0"}

print("🚀 Bot started!")

while True:
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            bot.send_message(CHAT_ID, "✅ O bot esta online e monitorando!")
        else:
            bot.send_message(CHAT_ID, f"❌ Erro ao acessar o site: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # Pausa de 60 segundos
    time.sleep(60)
