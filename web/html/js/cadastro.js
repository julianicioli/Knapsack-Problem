function cadastrarTransportadora(event) {
  // Impede a página de recarregar
  event.preventDefault();

  const senha = document.getElementById('senha').value;
  const confirmarSenha = document.getElementById('confirmar-senha').value;

  // Validação de senhas idênticas antes de enviar ao Python
  if (senha !== confirmarSenha) {
    alert("Erro: As senhas informadas não coincidem.");
    return;
  }

  // Desativa o botão para evitar cliques múltiplos
  const btn = document.getElementById('btn-cadastrar');
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<i class="ti ti-loader"></i> Cadastrando...`;
  }

  // Coleta os valores do formulário
  const dadosCadastro = {
    razao_social: document.getElementById('razao-social').value,
    nome_fantasia: document.getElementById('nome-fantasia').value,
    cnpj: document.getElementById('cnpj').value,
    telefone: document.getElementById('telefone').value,
    email: document.getElementById('email').value,
    endereco: document.getElementById('endereco').value,
    cidade: document.getElementById('cidade').value,
    estado: document.getElementById('estado').value,
    senha: senha
  };

  // Envia para a função correspondente no Python (main.py)
  eel.cadastrar_transportadora(dadosCadastro)(function(retorno) {
    if (retorno.status === "sucesso") {
      alert("Transportadora cadastrada com sucesso!");
      // Redireciona para a tela de login após dar OK
      window.location.href = "./login.html";
    } else if (retorno.status === "duplicado") {
      alert("Erro: Transportadora já cadastrada.");
      // Reativa o botão para correção
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = `Criar conta <i class="ti ti-user-plus"></i>`;
      }
    } else {
      alert("Erro ao realizar o cadastro: " + retorno.mensagem);
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = `Criar conta <i class="ti ti-user-plus"></i>`;
      }
    }
  });
}