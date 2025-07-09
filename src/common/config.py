import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SO = platform.system()

if SO == "Linux":
    CAMINHO_CHROMEDRIVER = "/usr/local/bin/chromedriver"
    CAMINHO_BRAVE = "/usr/bin/brave-browser"
elif SO == "Windows":
    CAMINHO_CHROMEDRIVER = "C:/chromedriver-win64/chromedriver.exe"
    CAMINHO_BRAVE = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
else:
    raise Exception(f"Sistema operacional não suportado: {SO}")
