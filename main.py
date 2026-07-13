import requests
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = "8952208320:AAFRmo8v5xk7GlnPm8qTd7WzQQPAnE2Y6QI"
CHAT_ID = "5805588750"

bot = telebot.TeleBot(TOKEN)

# Servidor simples para manter o bot online no Render
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

# Cabeçalho simulando um navegador Chrome real para evitar o erro 403
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

print("🚀 Bot started!")

while True:
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            bot.send_message(CHAT_ID, "✅ Site acessado com sucesso!")
        else:
            bot.send_message(CHAT_ID, f"❌ Erro ao acessar: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    time.sleep(60)
