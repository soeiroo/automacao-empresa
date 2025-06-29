# 🧾 Fechamento Automático dos PDVs (1 a 39)

Este programa automatiza o processo de **fechamento de caixa de todos os PDVs** da loja (do 1 ao 39), utilizando o navegador Brave e a biblioteca Selenium.

---

## 🚀 Funcionalidades

- Acessa automaticamente os endereços locais de cada PDV
- Simula os comandos de teclado usados no fechamento
- Aguarda 2 segundos entre cada PDV
- Exibe um log detalhado na interface durante a execução
- Fecha automaticamente o navegador ao final do processo

---

## 📋 PDVs processados

- **PDVs 1 a 39**
- ❌ **Exceções**:
  - **PDV 34** está desativado (não será processado)
  - **PDV 29** usa IP personalizado: http://192.168.222.179:9898/normal.html

---

## 🖥️ Requisitos do Sistema

### ✅ Requisitos obrigatórios:

| Requisito       | Detalhes                                                                 |
|-----------------|--------------------------------------------------------------------------|
| Python          | Versão 3.10 ou superior                                                   |
| Selenium        | Instalar com pip install selenium                                      |
| Brave Browser   | Deve estar instalado no caminho abaixo                                   |
| ChromeDriver    | Mesma versão do Chromium usado pelo Brave                                |

---

## 📦 Instalação dos Requisitos

### 🔹 1. Instale o Selenium

No terminal ou prompt de comando:
```bash
pip install selenium
```

---

### 🔹 2. Instale o Brave

Baixe o navegador Brave diretamente pelo site oficial:  
🔗 https://brave.com/pt-br/download/

O Brave deve estar instalado neste caminho padrão (necessário para o script funcionar):
```yaml
C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe
```

---

### 🔹 3. Instale o ChromeDriver

O ChromeDriver permite que o Selenium controle o Brave. Ele **deve ter a mesma versão do Chromium usada pelo Brave**.

#### Passos:
1. Abra o Brave e acesse:
```yaml
brave://version
```
2. Verifique a versão do Chromium (ex: `120.0.6099.71`)
3. Acesse o site oficial:
🔗 https://chromedriver.chromium.org/downloads
4. Baixe o ChromeDriver da **mesma versão**.
5. Extraia e coloque o `chromedriver.exe` em:
```yaml
C:/chromedriver-win64/chromedriver.exe
```

✅ **Dica:** mantenha o nome da pasta e o caminho exatos para evitar erros de execução.

---

## ▶️ Como usar

1. Certifique-se de que todos os requisitos estão instalados corretamente.
2. Execute o arquivo `fechamento_pdv.py` (ou `.exe`, se empacotado).
3. Uma janela será aberta com o botão **“Iniciar Fechamento”**.
4. Clique no botão e o sistema:
- Acessa automaticamente os endereços locais de cada PDV
- Simula os comandos de teclado usados no fechamento
- Executa o fechamento de todos os PDVs em sequência
- Exibe um log detalhado na interface durante a execução
- Fecha automaticamente o navegador ao final do processo

---

## ⚠️ Aviso de Responsabilidade

Este programa interage diretamente com os sistemas dos PDVs.  
Use com extrema responsabilidade:

- Apenas com **autorização da equipe de TI**
- Nunca execute durante o expediente da loja
- Sempre revise os comandos antes de usar

❗ Um erro pode afetar o funcionamento dos caixas, da rede ou do sistema interno da loja.

---
