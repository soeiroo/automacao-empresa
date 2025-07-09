# 🏢 Automação Empresa – Controle de PDVs com Python

Automação de processos internos para o gerenciamento e controle de Pontos de Venda (PDVs) em uma rede corporativa. Este projeto foi desenvolvido para facilitar tarefas repetitivas através de uma interface gráfica simples e uso de automação via Selenium.

![Badge](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Funcionalidades

- 🧠 **Automação Inteligente**: Automatiza ações repetitivas nos PDVs, ignorando máquinas fora do ar.
- 💻 **Interface Gráfica (Tkinter)**: Usabilidade simplificada com uma tela interativa.
- 🚀 **Execução Rápida em Lote**: Processa múltiplos PDVs em sequência.
- ⚠️ **Tratamento de Exceções**: Ignora PDVs específicos (como o 34) e prossegue sem travamentos.
- 🪪 **Login Automatizado**: Uso de Selenium para autenticação e execução remota.
- 🧩 **Configuração Centralizada**: Caminhos como `chromedriver` e `brave` são definidos em um único arquivo (`src/common/config.py`).
- 🧠 **Suporte Multiplataforma**: Detecta automaticamente se está rodando em Windows ou Linux.

---

## 🖼️ Demonstração

![screenshot](docs/image.png)

---

## 🛠️ Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [Brave Browser](https://brave.com/)

---

## 📦 Instalação

Clone o projeto:

```bash
git clone https://github.com/soeiroo/automacao-empresa.git
cd automacao-empresa
```

Instale os requisitos:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuração

Edite o arquivo `src/common/config.py` para garantir que os caminhos para o ChromeDriver e Brave estejam corretos para seu sistema.

O projeto já detecta automaticamente se você está em **Linux** ou **Windows**.

---

## ▶️ Como usar

1. Acesse a pasta `src`:

```bash
cd src
```

2. Execute o script principal com a interface:

```bash
python fechamento-automacaov2.py
```

3. Clique em **"Iniciar Fechamento"**.
4. O sistema passará por todos os PDVs (exceto os definidos como exceção, como o PDV 34).

---

## 📌 Exceções personalizadas

- PDVs podem ser excluídos do processo manualmente pela interface.
- Os PDV's **34 e 40** são ignorados automaticamente no script, por motivo de instabilidade.
- O PDV **41** possui um link personalizado já tratado no código.

---

## 🤝 Contribuições

Sinta-se livre para enviar pull requests ou abrir issues. Sugestões são bem-vindas!

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
