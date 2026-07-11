import requests
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Servidor para o Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active")

def run_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# Lógica do Robô
TOKEN = os.environ.get("TOKEN")
CHAT_ID = "@canaldowt"

print("🚀 Robô iniciado com sucesso (Método Rápido)!")

while True:
    try:
        # A API oficial do histórico do jogo
        url = "https://aviator.spribe.services/api/v1/history/aviator"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            if dados:
                ultima_vela = float(dados[0]['game_result'])
                print(f"🎰 Última vela: {ultima_vela}x")
                
                if ultima_vela >= 1.7:
                    mensagem = f"🚨 **Sinal Detectado!**\n\n📊 Vela anterior: {ultima_vela}x"
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                  data={"chat_id": CHAT_ID, "text": mensagem})
        
    except Exception as e:
        print(f"Aguardando dados... (Erro: {e})")
    
    time.sleep(5)
