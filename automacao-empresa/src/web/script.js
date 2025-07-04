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
  window.open(`http://${ip}`, '_blank');
  historico.push({ pdv: num, data: new Date().toISOString() });
  localStorage.setItem('historicoAcessos', JSON.stringify(historico));
}

function checarStatusPDVs() {
  let online = 0;
  const botoes = document.querySelectorAll('.pdv-btn');
  botoes.forEach((btn, idx) => {
    const num = idx + 1;
    const ip = num === 41 ? PDV_41_IP : PDV_BASE_IP + (PDV_START + num - 1);
    fetch(`http://${ip}`, { method: 'HEAD', mode: 'no-cors' })
      .then(() => {
        btn.querySelector('.status-dot').textContent = '🟢';
        online++;
        onlineCountSpan.textContent = online;
      })
      .catch(() => {
        btn.querySelector('.status-dot').textContent = '🔴';
        onlineCountSpan.textContent = online;
      });
  });
}

liberarBtn.onclick = () => {
  if (senhaInput.value === SENHA_PADRAO) {
    acessoLiberado = true;
    criarBotoesPDV();
  } else {
    alert('Senha incorreta!');
  }
};

window.onload = () => {
  criarBotoesPDV();
  setInterval(checarStatusPDVs, 5000);
  checarStatusPDVs();
};
