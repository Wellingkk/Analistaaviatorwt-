import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Usa o token como variável de ambiente
TOKEN = os.environ.get("TOKEN")
CHAT_ID = "@canaldowt"

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

print("🕵️ Inicializando navegador virtual no servidor...")
try:
    # O driver agora usará o ambiente padrão do container
    driver = webdriver.Chrome(options=chrome_options)

    url_jogo = "https://apostatudo.com/casino/game/spribe-aviator"
    print(f"🔗 Acessando: {url_jogo}")
    driver.get(url_jogo)
    time.sleep(10) 

    print("👀 Monitorando as rodadas reais...")
    velas_alvo = [1.06, 1.07, 1.09]
    ultima_vela = None

    while True:
        try:
            elementos = driver.find_elements(By.CSS_SELECTOR, ".payouts-block .bubble-multiplier")

            if elementos:
                texto_vela = elementos[0].text.replace('x', '').strip()

                try:
                    vela_atual = float(texto_vela)

                    if vela_atual != ultima_vela:
                        print(f"🎰 Rodada Real: Vela parou em {vela_atual}x")
                        ultima_vela = vela_atual

                        if vela_atual in velas_alvo:
                            print(f"🎯 ALERTA! Vela de {vela_atual}x detectada!")
                            mensagem = (
                                f"🚨 **SINAL CONFIRMADO!** 🚨\n\n"
                                f"📊 Vela Real: {vela_atual}x!\n"
                                "🎯 **Entrada:** Próxima rodada"
                            )
                            link_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                            requests.post(link_telegram, data={"chat_id": CHAT_ID, "text": mensagem})
                except ValueError:
                    pass
        except Exception as e_loop:
            print(f"⚠️ Erro no monitoramento: {e_loop}")
            
        time.sleep(3)

except Exception as e:
    print(f"❌ Ocorreu um problema sério: {e}")
