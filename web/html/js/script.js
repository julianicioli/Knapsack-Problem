let counter = 0;

<<<<<<< HEAD
// Garante que o sistema inicie criando pelo menos um card de item em segundo plano
window.addEventListener("DOMContentLoaded", () => {
  if (document.querySelectorAll('.item-card').length === 0) {
    addItem();
  }
});

// ======================
// Navegação entre telas (Ordem Invertida para Transporte -> Estoque)
// ======================

function irParaEstoque() {
  // Validação rápida: Garante que preencheram a capacidade antes de avançar
  const capacidade = document.getElementById('capacidade').value;
  if (!capacidade) {
    alert("Por favor, preencha a capacidade máxima de carga do veículo antes de prosseguir.");
    return;
  }

  // Oculta a Tela de Transporte (screen-2) e mostra a Tela de Estoque (screen-1)
  document.getElementById('screen-2').classList.add('hidden');
  document.getElementById('screen-1').classList.remove('hidden');

  // Atualiza as bolinhas indicadoras no topo
  document.getElementById('step-indicator-1').classList.remove('active');
  document.getElementById('step-indicator-2').classList.add('active');
}

function voltarParaTransporte() {
  // Oculta a Tela de Estoque (screen-1) e mostra a Tela de Transporte (screen-2)
  document.getElementById('screen-1').classList.add('hidden');
  document.getElementById('screen-2').classList.remove('hidden');

  // Atualiza as bolinhas indicadoras no topo
=======
// ======================
// Navegação entre telas
// ======================

function irParaTransporte() {
  document.getElementById('screen-1').classList.add('hidden');
  document.getElementById('screen-2').classList.remove('hidden');

  document.getElementById('step-indicator-1').classList.remove('active');
  document.getElementById('step-indicator-2').classList.add('active');

  if (document.querySelectorAll('.item-card').length === 0) {
    addItem();
  }
}

function voltarParaEstoque() {
  document.getElementById('screen-2').classList.add('hidden');
  document.getElementById('screen-1').classList.remove('hidden');

>>>>>>> 522a007256d658489c768dff5f9cb62fcc5327c4
  document.getElementById('step-indicator-2').classList.remove('active');
  document.getElementById('step-indicator-1').classList.add('active');
}

// ======================
// Itens do estoque
// ======================

function addItem() {
  counter++;

  const list = document.getElementById('items-list');
  const div = document.createElement('div');

  div.className = 'item-card';
  div.id = 'item-' + counter;

  div.innerHTML = `
    <div class="item-card-header">
      <span class="item-badge">Item #${counter}</span>
      <button
        class="remove-btn"
        onclick="removeItem(${counter})"
        title="Remover item">
        <i class="ti ti-x"></i>
      </button>
    </div>

    <div class="item-form">
      <div class="grid-2">
        <div class="field">
          <label>Tipo do Item</label>
          <input
            type="text"
            placeholder="Ex: Caixa, Palete..."
            data-field="tipo">
        </div>

        <div class="field">
          <label>Quantidade</label>
          <input
            type="number"
            placeholder="0"
<<<<<<< HEAD
            min="1"
            step="1"
            value="1"
=======
            min="0"
            step="1"
>>>>>>> 522a007256d658489c768dff5f9cb62fcc5327c4
            data-field="qtd"
            oninput="updateSummary()">
        </div>
      </div>

      <div class="grid-5">
        <div class="field">
          <label>Peso (kg)</label>
          <input
            type="number"
            placeholder="0,00"
            min="0"
            step="0.01"
            data-field="peso"
            oninput="updateSummary()">
        </div>

        <div class="field">
          <label>Comprimento (m)</label>
          <input
            type="number"
            placeholder="0,00"
            min="0"
            step="0.01"
            data-field="comprimento">
        </div>

        <div class="field">
          <label>Largura (m)</label>
          <input
            type="number"
            placeholder="0,00"
            min="0"
            step="0.01"
            data-field="largura">
        </div>

        <div class="field">
          <label>Altura (m)</label>
          <input
            type="number"
            placeholder="0,00"
            min="0"
            step="0.01"
            data-field="altura">
        </div>

        <div class="field">
          <label>Valor (R$)</label>
          <input
            type="number"
            placeholder="0,00"
            min="0"
            step="0.01"
            data-field="valor"
            oninput="updateSummary()">
        </div>
      </div>

      <div class="field">
        <label>Observações</label>
        <textarea
          placeholder="Informações adicionais..."
          data-field="obs"></textarea>
      </div>
    </div>
  `;

  list.appendChild(div);
  updateSummary();
}

function removeItem(id) {
  const item = document.getElementById('item-' + id);
  if (item) {
    item.remove();
  }
  updateSummary();
}

// ======================
// Resumo dinâmico
// ======================

function updateSummary() {
  const cards = document.querySelectorAll('.item-card');
  let totalPeso = 0;
  let totalValor = 0;

  cards.forEach(card => {
    const peso = parseFloat(card.querySelector('[data-field="peso"]').value) || 0;
    const qtd = parseFloat(card.querySelector('[data-field="qtd"]').value) || 1;
    const valor = parseFloat(card.querySelector('[data-field="valor"]').value) || 0;

    totalPeso += peso * qtd;
    totalValor += valor * qtd;
  });

  document.getElementById('total-itens').textContent = cards.length;
  document.getElementById('total-peso').textContent = totalPeso.toFixed(2).replace('.', ',');
  document.getElementById('total-valor').textContent = totalValor.toFixed(2).replace('.', ',');
}

// ======================
// Comunicação com o Backend (Eel)
// ======================
<<<<<<< HEAD
=======

>>>>>>> 522a007256d658489c768dff5f9cb62fcc5327c4
function salvar() {
  const cards = document.querySelectorAll('.item-card');
  
  if (cards.length === 0) {
    alert("Adicione pelo menos um item ao estoque antes de salvar.");
    return;
  }

<<<<<<< HEAD
=======
  // 1. Monta o objeto de transporte a partir dos inputs do HTML
>>>>>>> 522a007256d658489c768dff5f9cb62fcc5327c4
  const transporte = {
    motorista: document.getElementById('name').value,
    placa: document.getElementById('placa').value,
    tipo: document.getElementById('transporte').value,
    carga: document.getElementById('carga').value,
    comprimento: document.getElementById('comprimento-transporte').value,
    largura: document.getElementById('largura-transporte').value,
    altura: document.getElementById('altura-transporte').value,
    capacidade: document.getElementById('capacidade').value,
    destino: document.getElementById('destino').value,
    saida: document.getElementById('saida').value,
    chegada: document.getElementById('chegada').value,
    observacoes: document.getElementById('obs-transporte').value
  };

  if (!transporte.capacidade) {
<<<<<<< HEAD
    alert("Erro: Informações de transporte ausentes. Por favor, volte e preencha a capacidade do veículo.");
    return;
  }

  const itens = [];
  cards.forEach(card => {
    itens.push({
      nome: card.querySelector('[data-field="tipo"]').value || 'Item Sem Nome',
      peso: parseFloat(card.querySelector('[data-field="peso"]').value) || 0,
      valor: parseFloat(card.querySelector('[data-field="valor"]').value) || 0
    });
  });

  // Trava o botão para evitar cliques duplicados
  const botaoSalvar = document.querySelector("button[onclick='salvar()']");
  if (botaoSalvar) {
    botaoSalvar.disabled = true;
    botaoSalvar.innerHTML = `<i class="ti ti-loader"></i> Processando...`;
    botaoSalvar.style.opacity = "0.6";
    botaoSalvar.style.cursor = "not-allowed";
  }

  console.log("Enviando dados estruturados para otimização via Python:", itens);

  eel.resolver_mochila(transporte.capacidade, itens)(function(retorno) {
    if (retorno && retorno.valor_otimizado !== undefined) {
      
      // Remove o hidden do bloco de resultado caso ele esteja invisível
      const blocoResultado = document.getElementById('bloco-resultado-mochila');
      if (blocoResultado) {
        blocoResultado.classList.remove('hidden');
      }

      // Procura o parágrafo de valor total (seja dentro da ID ou da classe antiga de fallback)
      let pValor = document.querySelector('#bloco-resultado-mochila p:nth-of-type(1)');
      if (!pValor) {
        pValor = document.querySelector('.field-calculo p:nth-of-type(1)');
      }
      if (pValor) {
        pValor.innerHTML = `<strong>Valor Total Otimizado:</strong> R$ ${retorno.valor_otimizado.toFixed(2).replace('.', ',')}`;
      }

      // Procura a lista ul para injetar os itens dinamicamente
      let listaItensContainer = document.querySelector('#bloco-resultado-mochila ul');
      if (!listaItensContainer) {
        listaItensContainer = document.querySelector('.field-calculo ul');
      }
      
      if (listaItensContainer) {
        listaItensContainer.innerHTML = "";

        if (retorno.itens_escolhidos.length === 0) {
          listaItensContainer.innerHTML = "<li>Nenhum item coube nos critérios de peso da mochila.</li>";
        } else {
          retorno.itens_escolhidos.forEach(item => {
            const li = document.createElement('li');
            li.style.margin = "6px 0";
            li.innerHTML = `📦 <strong>${item.nome}</strong> — Peso: ${item.peso} kg | Valor: R$ ${item.valor.toFixed(2).replace('.', ',')}`;
            listaItensContainer.appendChild(li);
          });
        }
      }

      if (botaoSalvar) {
        botaoSalvar.innerHTML = `<i class="ti ti-check"></i> Concluído`;
      }

      const msg = document.getElementById('success-msg');
      if (msg) {
        document.getElementById('success-text').textContent = "Otimização concluída e gravada com sucesso!";
        msg.style.display = 'flex';
        setTimeout(() => { msg.style.display = 'none'; }, 4000);
      }

    } else {
      alert("Erro ao processar o algoritmo da mochila no Python.");
      if (botaoSalvar) {
        botaoSalvar.disabled = false;
        botaoSalvar.innerHTML = `<i class="ti ti-device-floppy"></i> Salvar Tudo`;
        botaoSalvar.style.opacity = "1";
        botaoSalvar.style.cursor = "pointer";
      }
=======
    alert("Por favor, preencha a capacidade máxima de carga do veículo.");
    return;
  }

  // 2. Extrai a lista de itens inseridos dinamicamente nos cards
  const itens = [];
  cards.forEach(card => {
    itens.push({
      tipo: card.querySelector('[data-field="tipo"]').value || 'Item Sem Nome',
      quantidade: card.querySelector('[data-field="qtd"]').value || 1,
      peso: card.querySelector('[data-field="peso"]').value || 0,
      comprimento: card.querySelector('[data-field="comprimento"]').value || 0,
      largura: card.querySelector('[data-field="largura"]').value || 0,
      altura: card.querySelector('[data-field="altura"]').value || 0,
      valor: card.querySelector('[data-field="valor"]').value || 0,
      observacoes: card.querySelector('[data-field="obs"]').value || ''
    });
  });

  console.log("Enviando dados estruturados para otimização via Python:", { transporte, itens });

  // 3. Executa a chamada remota para o Controller no Python
  eel.otimizar_e_salvar(transporte, itens)(function(retorno) {
    if (retorno.sucesso) {
      const msg = document.getElementById('success-msg');
      document.getElementById('success-text').textContent = 
        `Otimizado com sucesso! Valor total na mochila: R$ ${retorno.valor_total.toFixed(2)}`;
      
      msg.style.display = 'flex';
      
      setTimeout(() => {
        msg.style.display = 'none';
      }, 4000);

      console.log("Mochila calculada. Itens selecionados para embarque:", retorno.itens_escolhidos);
    } else {
      alert("Erro de persistência: O algoritmo processou, mas os dados não puderam ser gravados no MySQL.");
>>>>>>> 522a007256d658489c768dff5f9cb62fcc5327c4
    }
  });
}