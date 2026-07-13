import requests
import time
import os
import threading
import telebot
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- CONFIGURAÇÕES ---
# Pegue o token no BotFather
TOKEN = "SEU_TOKEN_DO_BOT_AQUI" 
# O @ do seu canal ou o ID numérico
CHAT_ID = "@seu_canal_ou_id" 

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

# Inicia o servidor web para o Render não derrubar o bot
threading.Thread(target=run_server, daemon=True).start()

URL = "https://tipminer.com/aviator"
headers = {"User-Agent": "Mozilla/5.0"}

print("🚀 Bot started!")

while True:
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            # Aqui você processa o dado do site conforme sua necessidade
            msg = "✅ O bot está monitorando o site normalmente."
            bot.send_message(CHAT_ID, msg)
        else:
            bot.send_message(CHAT_ID, f"❌ Erro ao acessar o site: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        bot.send_message(CHAT_ID, f"⚠️ Erro no bot: {str(e)}")
    
    # Pausa de 30 segundos entre as verificações
    time.sleep(30)
