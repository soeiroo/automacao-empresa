@echo off
REM Instala o Flask se não estiver instalado
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Instalando Flask...
    pip install flask
)

REM Inicia o backend Python para status dos PDVs em segundo plano
cd /d "%~dp0"
start "BackendPython" /min python src\web\ping_server.py

REM Aguarda 2 segundos para garantir que o backend subiu
timeout /t 2 >nul

REM Abre o aplicativo Electron na pasta src e fecha o terminal
cd src
start "ElectronApp" /min cmd /c "npm start"
cd ..

REM Mensagem para o usuário
echo Tudo iniciado! Pode fechar esta janela se quiser.
exit
