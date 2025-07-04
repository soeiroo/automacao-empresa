const PDV_COUNT = 41;
const PDV_41_IP = '192.168.222.179';
const PDV_BASE_IP = '192.168.222.';
const PDV_START = 101;
const PDV_END = 140;
const SENHA_PADRAO = '1234';

const senhaInput = document.getElementById('senha');
const liberarBtn = document.getElementById('liberar');
const pdvButtonsDiv = document.getElementById('pdv-buttons');
const onlineCountSpan = document.getElementById('online-count');

let acessoLiberado = false;
let historico = JSON.parse(localStorage.getItem('historicoAcessos') || '[]');

function criarBotoesPDV() {
  pdvButtonsDiv.innerHTML = '';
  for (let i = 1; i <= PDV_COUNT; i++) {
    const btn = document.createElement('button');
    btn.className = 'pdv-btn' + (i === 41 ? ' pdv-41' : '');
    btn.textContent = `PDV ${i}`;
    btn.disabled = !acessoLiberado;
    btn.dataset.pdv = i;
    btn.innerHTML += ' <span class="status-dot">🔴</span>';
    btn.onclick = () => abrirPDV(i);
    pdvButtonsDiv.appendChild(btn);
  }
}

function abrirPDV(num) {
  const ip = num === 41 ? PDV_41_IP : PDV_BASE_IP + (PDV_START + num - 1);
  window.open(`http://${ip}:9898/normal.html`, '_blank');
  historico.push({ pdv: num, data: new Date().toISOString() });
  localStorage.setItem('historicoAcessos', JSON.stringify(historico));
}

async function checarStatusPDVs() {
  let online = 0;
  const botoes = document.querySelectorAll('.pdv-btn');
  for (let idx = 0; idx < botoes.length; idx++) {
    const btn = botoes[idx];
    const num = idx + 1;
    const ip = num === 41 ? PDV_41_IP : PDV_BASE_IP + (PDV_START + num - 1);
    let statusOnline = false;
    if (window.pdvAPI && window.pdvAPI.pingPDV) {
      try {
        statusOnline = await window.pdvAPI.pingPDV(ip);
      } catch (e) {
        statusOnline = false;
      }
    }
    btn.querySelector('.status-dot').textContent = statusOnline ? '🟢' : '🔴';
    if (statusOnline) online++;
  }
  onlineCountSpan.textContent = online;
}

liberarBtn.onclick = () => {
  if (senhaInput.value === SENHA_PADRAO) {
    acessoLiberado = true;
    criarBotoesPDV();
    checarStatusPDVs(); // Atualiza status após liberar acesso
  } else {
    alert('Senha incorreta!');
  }
};

window.onload = () => {
  criarBotoesPDV();
  checarStatusPDVs(); // Checa status só uma vez ao abrir o site
};
