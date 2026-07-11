import time
import requests
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- Servidor para manter o Render "feliz" ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    server = HTTPServer(('0.0.0.0', int(os.environ.get("PORT", 8080))), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# --- Configuração do Robô ---
TOKEN = os.environ.get("TOKEN")
CHAT_ID = "@canaldowt"

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = "/usr/bin/chromium"

print("🕵️ Inicializando robô...")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://apostatudo.com/casino/game/spribe-aviator")
time.sleep(10)

ultima_vela = None
while True:
    try:
        elementos = driver.find_elements(By.CSS_SELECTOR, ".bubble-multiplier")
        if elementos:
            texto = elementos[0].text.replace('x', '')
            vela_atual = float(texto)
            if vela_atual != ultima_vela:
                print(f"🎰 Vela: {vela_atual}x")
                ultima_vela = vela_atual
                if vela_atual >= 1.7:
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                                  data={"chat_id": CHAT_ID, "text": f"🚨 Vela {vela_atual}x detectada!"})
    except Exception as e:
        pass
    time.sleep(2)
