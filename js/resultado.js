const resultado = {
  pesoUtilizado: "850 / 1000 kg",
  volumeUtilizado: "18 / 20 m³",
  valorTotal: "R$ 24.500",

  selecionados: [
    {
      nome: "Notebook Dell",
      peso: "20 kg",
      valor: "R$ 5.000"
    },
    {
      nome: "Monitor LG",
      peso: "15 kg",
      valor: "R$ 2.000"
    },
    {
      nome: "Impressora HP",
      peso: "35 kg",
      valor: "R$ 1.800"
    }
  ],

  rejeitados: [
    {
      nome: "Geladeira Industrial",
      peso: "120 kg",
      valor: "R$ 3.500"
    },
    {
      nome: "Armário Metálico",
      peso: "80 kg",
      valor: "R$ 1.500"
    }
  ]
};

document.getElementById("peso-utilizado").textContent =
resultado.pesoUtilizado;

document.getElementById("volume-utilizado").textContent =
resultado.volumeUtilizado;

document.getElementById("valor-total").textContent =
resultado.valorTotal;

const selecionados =
document.getElementById("itens-selecionados");

resultado.selecionados.forEach(item => {

  selecionados.innerHTML += `
    <div class="item-card">
      <span>${item.nome}</span>
      <span>${item.peso}</span>
      <span>${item.valor}</span>
    </div>
  `;

});

const rejeitados =
document.getElementById("itens-rejeitados");

resultado.rejeitados.forEach(item => {

  rejeitados.innerHTML += `
    <div class="item-card rejected">
      <span>${item.nome}</span>
      <span>${item.peso}</span>
      <span>${item.valor}</span>
    </div>
  `;

});