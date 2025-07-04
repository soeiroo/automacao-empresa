import subprocess
import json
from flask import Flask, jsonify

app = Flask(__name__)

PDV_COUNT = 41
PDV_41_IP = '192.168.222.179'
PDV_BASE_IP = '192.168.222.'
PDV_START = 101

# Gera lista de IPs
ips = [PDV_BASE_IP + str(PDV_START + i - 1) for i in range(1, PDV_COUNT)]
ips.append(PDV_41_IP)

def ping(ip):
    try:
        # -n 1: 1 pacote, -w 500: timeout 500ms
        output = subprocess.run(['ping', '-n', '1', '-w', '500', ip], capture_output=True, text=True)
        return output.returncode == 0
    except Exception:
        return False

@app.route('/status')
def status():
    result = {}
    for idx, ip in enumerate(ips, 1):
        result[str(idx)] = ping(ip)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
