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

print("🚀 Robô iniciado com sucesso (Sem Selenium)!")

while True:
    try:
        # A API retorna o histórico
        url = "https://aviator.spribe.services/api/v1/history/aviator"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            if dados:
                ultima_vela = float(dados[0]['game_result'])
                print(f"🎰 Última vela: {ultima_vela}x")
                
                # A lógica de envio para o Telegram
                token = os.environ.get("TOKEN")
                chat_id = "@canaldowt"
                if ultima_vela >= 1.7:
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                                  data={"chat_id": chat_id, "text": f"🚨 Vela {ultima_vela}x detectada!"})
        
    except Exception as e:
        print(f"Aguardando dados... (Erro: {e})")
    
    time.sleep(10)
