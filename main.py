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

TOKEN = os.environ.get("TOKEN")
CHAT_ID = "@canaldowt"

print("🚀 Robô iniciado (Modo Requisição Direta)!")

# Cabeçalho para fingir ser um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

while True:
    try:
        # Tenta acessar o site principal (às vezes o DNS do Render tem problemas com subdomínios de API)
        response = requests.get("https://apostatudo.com/casino/game/spribe-aviator", headers=headers, timeout=15)
        
        if response.status_code == 200:
            print("✅ Site acessado. Verificando dados...")
            # Aqui entraríamos na lógica de extração se o site retornar os dados no HTML
        else:
            print(f"❌ Erro ao acessar: {response.status_code}")
            
    except Exception as e:
        print(f"Aguardando... (Erro de conexão: {e})")
    
    time.sleep(15)
