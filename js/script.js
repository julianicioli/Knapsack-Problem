let counter = 0;

// ── Navegação entre telas ──

function irParaItens() {
  document.getElementById('screen-1').classList.add('hidden');
  document.getElementById('screen-2').classList.remove('hidden');
  document.getElementById('step-indicator-1').classList.remove('active');
  document.getElementById('step-indicator-2').classList.add('active');

  if (document.querySelectorAll('.item-card').length === 0) {
    addItem();
  }
}

function voltarParaTransporte() {
  document.getElementById('screen-2').classList.add('hidden');
  document.getElementById('screen-1').classList.remove('hidden');
  document.getElementById('step-indicator-2').classList.remove('active');
  document.getElementById('step-indicator-1').classList.add('active');
}

// ── Gerenciamento de itens ──

function addItem() {
  counter++;
  const list = document.getElementById('items-list');
  const div = document.createElement('div');
  div.className = 'item-card';
  div.id = 'item-' + counter;
  div.innerHTML = `
    <div class="item-card-header">
      <span class="item-badge">Item #${counter}</span>
      <button class="remove-btn" onclick="removeItem(${counter})" title="Remover item ${counter}">
        <i class="ti ti-x"></i>
      </button>
    </div>
    <div class="item-form">
      <div class="grid-2">
        <div class="field">
          <label>Tipo do item</label>
          <input type="text" placeholder="Ex: Caixa, Palete..." data-field="tipo" />
        </div>
        <div class="field">
          <label>Quantidade</label>
          <input type="number" placeholder="0" step="0.01" min="0" data-field="qtd" oninput="updateSummary()" />
        </div>
      </div>
      <div class="grid-3">
        <div class="field">
          <label>Peso (kg)</label>
          <input type="number" placeholder="0,00" step="0.01" min="0" data-field="peso" oninput="updateSummary()" />
        </div>
        <div class="field">
          <label>Dimensão (m³)</label>
          <input type="number" placeholder="0,00" step="0.01" min="0" data-field="medida" />
        </div>
        <div class="field">
          <label>Valor (R$)</label>
          <input type="number" placeholder="0,00" step="0.01" min="0" data-field="valor" oninput="updateSummary()" />
        </div>
      </div>
      <div class="field">
        <label>Observações</label>
        <textarea placeholder="Informações adicionais..." data-field="obs"></textarea>
      </div>
    </div>
  `;
  list.appendChild(div);
  updateSummary();
}

function removeItem(id) {
  const el = document.getElementById('item-' + id);
  if (el) el.remove();
  updateSummary();
}

function updateSummary() {
  const cards = document.querySelectorAll('.item-card');
  let totalPeso = 0, totalValor = 0;

  cards.forEach(card => {
    const peso  = parseFloat(card.querySelector('[data-field="peso"]').value) || 0;
    const qtd   = parseFloat(card.querySelector('[data-field="qtd"]').value)  || 1;
    const valor = parseFloat(card.querySelector('[data-field="valor"]').value) || 0;
    totalPeso  += peso * qtd;
    totalValor += valor * qtd;
  });

  document.getElementById('total-itens').textContent = cards.length;
  document.getElementById('total-peso').textContent   = totalPeso.toFixed(2).replace('.', ',');
  document.getElementById('total-valor').textContent  = totalValor.toFixed(2).replace('.', ',');
}

// ── Salvar ──

function salvar() {
  const cards = document.querySelectorAll('.item-card');
  if (cards.length === 0) {
    alert('Adicione ao menos um item antes de salvar.');
    return;
  }

  // Dados do transporte
  const transporte = {
    motorista:   document.getElementById('name').value,
    placa:       document.getElementById('placa').value,
    tipo:        document.getElementById('transporte').value,
    carga:       document.getElementById('carga').value,
    dimensao:    document.getElementById('dimensao').value,
    capacidade:  document.getElementById('capacidade').value,
    destino:     document.getElementById('destino').value,
    saida:       document.getElementById('saida').value,
    chegada:     document.getElementById('chegada').value,
    observacoes: document.getElementById('obs-transporte').value,
  };

  // Dados dos itens
  const itens = [];
  cards.forEach(card => {
    itens.push({
      tipo:        card.querySelector('[data-field="tipo"]').value,
      quantidade:  card.querySelector('[data-field="qtd"]').value,
      peso:        card.querySelector('[data-field="peso"]').value,
      medida:      card.querySelector('[data-field="medida"]').value,
      valor:       card.querySelector('[data-field="valor"]').value,
      observacoes: card.querySelector('[data-field="obs"]').value,
    });
  });

  // Envio ao backend (descomente e ajuste a URL conforme necessário):
  // fetch('/api/cadastro', {
  //   method: 'POST',
  //   headers: { 'Content-Type': 'application/json' },
  //   body: JSON.stringify({ transporte, itens })
  // });

  console.log('Cadastro completo:', { transporte, itens });

  const msg = document.getElementById('success-msg');
  document.getElementById('success-text').textContent =
    `${cards.length} item(s) salvo(s) com sucesso!`;
  msg.style.display = 'flex';
  setTimeout(() => msg.style.display = 'none', 3500);
}
