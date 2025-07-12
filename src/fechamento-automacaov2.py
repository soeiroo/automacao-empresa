import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import threading
import time
from datetime import datetime
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
common_path = os.path.join(current_dir, "common")
sys.path.append(common_path)

from config import CAMINHO_CHROMEDRIVER, CAMINHO_BRAVE

def iniciar_fechamento(log_func, cracha, senha, pdv_inicio, pdv_fim, ignorar_pdvs, salvar_log, modo_simulacao):
    if not modo_simulacao:
        options = webdriver.ChromeOptions()
        options.binary_location = CAMINHO_BRAVE
        service = Service(executable_path=CAMINHO_CHROMEDRIVER)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = None

    desativados = [34, 40]
    personalizados = {41: "http://192.168.222.179:9898/normal.html"}
    ignorar_pdvs = set(desativados + ignorar_pdvs)

    for pdv in range(pdv_inicio, pdv_fim + 1):
        if pdv in ignorar_pdvs:
            log_func(f"⏭️ Pulando PDV {pdv} (ignorado ou desativado)\n")
            continue

        url = personalizados.get(pdv, f"http://192.168.222.{100 + pdv}:9898/normal.html")
        log_func(f"{'🧪 Simulando' if modo_simulacao else '▶️ Verificando status e fechando'} PDV {pdv}...")

        if modo_simulacao:
            time.sleep(0.5)
            log_func(f"✅ (Simulado) PDV {pdv} fechado com crachá {cracha} e senha {senha}.\n")
            continue

        try:
            driver.get(url)
        except Exception as acesso_erro:
            log_func(f"⚠️ PDV {pdv} fora do ar ou inacessível: {acesso_erro}\n")
            continue

        time.sleep(1)

        try:
            div = driver.find_element(By.CSS_SELECTOR, 'div[style="display: inline-block; width: 50%; text-align: center; overflow: hidden; white-space: nowrap;"]')
            texto_div = div.text.strip().lower()

            if "fechado parcial" in texto_div:
                log_func(f"🔍 PDV {pdv} com status 'Fechado Parcial', iniciando fechamento...")
            elif "fechado" in texto_div:
                log_func(f"ℹ️ PDV {pdv} já está fechado. Pulando...\n")
                continue
            elif "disponível" in texto_div or "disponivel" in texto_div:
                log_func(f"🔓 PDV {pdv} ainda está disponível. Pulando...\n")
                continue
            else:
                log_func(f"⚠️ PDV {pdv} com status não reconhecido: '{texto_div}', pulando...\n")
                continue
        except Exception:
            log_func(f"⚠️ PDV {pdv}: div de status não encontrada, pulando...\n")
            continue

        try:
            try:
                input_elem = driver.find_element(By.TAG_NAME, 'input')
                input_elem.click()
                input_elem.clear()
                body = input_elem
            except Exception:
                body = driver.find_element(By.TAG_NAME, 'body')
                body.click()

            time.sleep(0.3)
            body.send_keys("112")
            time.sleep(0.3)
            body.send_keys(Keys.TAB)
            time.sleep(0.3)

            driver.refresh()
            time.sleep(1)

            try:
                input_elem = driver.find_element(By.TAG_NAME, 'input')
                input_elem.click()
                input_elem.clear()
                body = input_elem
            except Exception:
                body = driver.find_element(By.TAG_NAME, 'body')
                body.click()

            body.send_keys(cracha)
            time.sleep(0.3)
            body.send_keys(Keys.ENTER)
            time.sleep(0.3)
            body.send_keys(senha)
            time.sleep(0.3)
            body.send_keys(Keys.ENTER)
            time.sleep(0.3)
            body.send_keys(Keys.ESCAPE)
            time.sleep(0.6)

            log_func(f"✅ PDV {pdv} fechado com sucesso.\n")
        except Exception as e:
            log_func(f"❌ Erro no PDV {pdv}: {e}\n")

    if driver:
        driver.quit()

    log_func("✅ Processo concluído!")

    with open("log_fechamento_PDVs.txt", "w", encoding="utf-8") as f:
        f.write(salvar_log.get("1.0", tk.END))

def criar_interface():
    janela = tk.Tk()
    janela.title("Fechamento de PDVs")
    janela.geometry("700x640")

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="Crachá:").grid(row=0, column=0, padx=5, sticky="e")
    entrada_cracha = tk.Entry(frame_inputs)
    entrada_cracha.grid(row=0, column=1, padx=5)

    tk.Label(frame_inputs, text="Senha Supervisor:").grid(row=0, column=2, padx=5, sticky="e")
    entrada_senha = tk.Entry(frame_inputs, show="*")
    entrada_senha.grid(row=0, column=3, padx=5)

    tk.Label(frame_inputs, text="PDV Inicial:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entrada_pdv_inicio = tk.Entry(frame_inputs, width=5)
    entrada_pdv_inicio.grid(row=1, column=1, padx=5)

    tk.Label(frame_inputs, text="PDV Final:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    entrada_pdv_fim = tk.Entry(frame_inputs, width=5)
    entrada_pdv_fim.grid(row=1, column=3, padx=5)

    tk.Label(frame_inputs, text="PDVs para ignorar (ex: 35,40,45):").grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="e")
    entrada_ignorar = tk.Entry(frame_inputs, width=25)
    entrada_ignorar.grid(row=2, column=2, columnspan=2, padx=5)

    modo_simulacao_var = tk.BooleanVar()
    checkbox_simulacao = tk.Checkbutton(janela, text="✔️ Modo Simulação (não abre navegador)", variable=modo_simulacao_var)
    checkbox_simulacao.pack()

    log_area = ScrolledText(janela, font=("Consolas", 10), width=85, height=23)
    log_area.pack(pady=10)

    botao = tk.Button(janela, text="Iniciar Fechamento", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")

    def log(texto):
        timestamp = datetime.now().strftime("[%H:%M:%S] ")
        log_area.insert(tk.END, timestamp + texto + "\n")
        log_area.see(tk.END)
        janela.update_idletasks()

    def on_click():
        cracha = entrada_cracha.get().strip()
        senha = entrada_senha.get().strip()
        ignorar_raw = entrada_ignorar.get().strip()
        modo_simulacao = modo_simulacao_var.get()

        try:
            pdv_inicio = int(entrada_pdv_inicio.get().strip())
            pdv_fim = int(entrada_pdv_fim.get().strip())
        except ValueError:
            log("❌ PDV Inicial e Final devem ser números inteiros.")
            return

        if not cracha or not senha:
            log("❌ Crachá e senha não podem estar vazios.")
            return
        if pdv_inicio > pdv_fim:
            log("❌ PDV Inicial não pode ser maior que o Final.")
            return

        ignorar_pdvs = []
        if ignorar_raw:
            try:
                ignorar_pdvs = [int(p.strip()) for p in ignorar_raw.split(",") if p.strip().isdigit()]
            except ValueError:
                log("❌ Lista de PDVs para ignorar inválida.")
                return

        botao.config(state=tk.DISABLED, text="Executando...")

        thread = threading.Thread(target=lambda: [
            iniciar_fechamento(log, cracha, senha, pdv_inicio, pdv_fim, ignorar_pdvs, log_area, modo_simulacao),
            botao.config(state=tk.NORMAL, text="Iniciar Fechamento")
        ])
        thread.start()

    botao.config(command=on_click)
    botao.pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
