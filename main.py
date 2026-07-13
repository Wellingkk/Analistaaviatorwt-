import requests
import time
import os

# Seu código do servidor (HTTPServer) continua igual aqui em cima...

# URL do histórico (Use o link que você quer monitorar)
URL = "https://tipminer.com/aviator" # Exemplo, ajuste se necessário

def monitorar():
    while True:
        try:
            response = requests.get(URL, headers=headers, timeout=15)
            if response.status_code == 200:
                # Vamos verificar se o texto "x" (ex: 2.50x) aparece no conteúdo
                if "x" in response.text:
                    print("✅ Dados recebidos com sucesso!")
                else:
                    print("⚠️ Site acessado, mas as velas não foram encontradas no HTML (provavelmente carregadas por JS).")
            else:
                print(f"❌ Erro HTTP: {response.status_code}")
        except Exception as e:
            print(f"❌ Erro de conexão: {e}")
        
        time.sleep(20)

# Inicie a thread do monitoramento
# (Lembre-se de manter o seu threading.Thread rodando)
