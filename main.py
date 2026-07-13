import requests
import time
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active")

def run_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

URL = "https://tipminer.com/aviator"
headers = {"User-Agent": "Mozilla/5.0"}

print("🚀 Robô iniciado!")

while True:
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        if response.status_code == 200:
            print("✅ Site acessado com sucesso.")
        else:
            print(f"❌ Erro HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    time.sleep(30)
