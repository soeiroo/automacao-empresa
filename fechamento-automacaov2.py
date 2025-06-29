import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time

# ======================= CONFIGURAÇÃO ==========================
CAMINHO_CHROMEDRIVER = "C:/chromedriver_win32/chromedriver.exe"
CAMINHO_BRAVE = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# ==============================================================

def iniciar_fechamento(log_func):
    options = webdriver.ChromeOptions()
    options.binary_location = CAMINHO_BRAVE
    driver = webdriver.Chrome(executable_path=CAMINHO_CHROMEDRIVER, options=options)

    desativados = [34]
    personalizados = {41: "http://192.168.222.179:9898/normal.html"}

    def fechar_pdv(url, pdv_num):
        try:
            log_func(f"▶️ Fechando PDV {pdv_num}...")

            try:
                driver.get(url)
            except Exception as acesso_erro:
                log_func(f"⚠️ PDV {pdv_num} fora do ar ou inacessível: {acesso_erro}\n")
                return

            time.sleep(0.7)

            body = driver.find_element(By.TAG_NAME, 'body')

            body.send_keys("112")
            time.sleep(0.3)
            body.send_keys(Keys.TAB)
            time.sleep(0.3)
            body.send_keys("460794")
            time.sleep(0.3)
            body.send_keys(Keys.ENTER)
            time.sleep(0.3)
            body.send_keys("123")
            time.sleep(0.3)
            body.send_keys(Keys.ENTER)
            time.sleep(0.3)

            log_func(f"✅ PDV {pdv_num} fechado com sucesso.\n")
        except Exception as e:
            log_func(f"❌ Erro no PDV {pdv_num}: {e}\n")

    for pdv in range(1, 42):
        if pdv in desativados:
            log_func(f"⏭️ Pulando PDV {pdv} (desativado)\n")
            continue

        url = personalizados.get(pdv, f"http://192.168.222.{100 + pdv}:9898/normal.html")
        fechar_pdv(url, pdv)

    driver.quit()
    log_func("✅ Processo concluído!")

def criar_interface():
    janela = tk.Tk()
    janela.title("Fechamento de PDVs")
    janela.geometry("600x400")

    botao = tk.Button(janela, text="Iniciar Fechamento", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
    log_area = ScrolledText(janela, font=("Consolas", 10), width=70, height=20)
    log_area.pack(pady=10)

    def log(texto):
        log_area.insert(tk.END, texto + "\n")
        log_area.see(tk.END)
        janela.update_idletasks()

    def on_click():
        botao.config(state=tk.DISABLED, text="Executando...")
        thread = threading.Thread(target=lambda: [iniciar_fechamento(log), botao.config(state=tk.NORMAL, text="Iniciar Fechamento")])
        thread.start()

    botao.config(command=on_click)
    botao.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
