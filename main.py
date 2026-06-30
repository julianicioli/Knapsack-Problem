import eel
import os
import sys
from controller.mochila_controller import MochilaController

# Garante que o Python reconheça os caminhos das pastas localmente
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Instancia o controlador globalmente para ser usado nas funções do Eel
controller = MochilaController()

# Lista temporária em memória para simular o banco de dados de transportadoras cadastradas
cnpjs_cadastrados_no_sistema = []

# ========================================================
# 1. FUNÇÃO QUE EXECUTA O CÁLCULO DA MOCHILA (CONEXÃO COM HTML)
# ========================================================

@eel.expose
def resolver_mochila(capacidade_max, lista_itens):
    print(f"\n====== EXECUTANDO ALGORITMO DA MOCHILA ======")
    print(f"Capacidade Máxima do Caminhão: {capacidade_max} kg")
    print(f"Itens Disponíveis no Estoque: {lista_itens}")
    print("=============================================\n")
    
    try:
        # Tratamento seguro para capacidade vazia ou nula
        if not capacidade_max or str(capacidade_max).strip() == "":
            capacidade_max = 0
        W = int(float(capacidade_max))
        
        # Filtra e limpa os itens vindos da tela
        itens = []
        for item in lista_itens:
            raw_peso = item.get("peso")
            raw_valor = item.get("valor")

            # Se o campo veio vazio do HTML, define como 0
            val_peso = 0 if (raw_peso == "" or raw_peso is None) else raw_peso
            val_valor = 0 if (raw_valor == "" or raw_valor is None) else raw_valor

            peso = int(float(val_peso))
            valor = float(val_valor)
            
            # Só processa se o item tiver peso e valor válidos
            if peso > 0 and valor > 0:
                itens.append({
                    "nome": str(item.get("nome", "Item")),
                    "peso": peso,
                    "valor": valor
                })
        
        n = len(itens)
        
        # Se não houver itens ou a capacidade for zero
        if n == 0 or W == 0:
            print("[AVISO] Nenhum item válido inserido ou capacidade igual a zero.")
            return {"valor_otimizado": 0.0, "itens_escolhidos": []}

        # Criando a tabela para Programação Dinâmica (Matriz n+1 x W+1)
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]

        # Construindo a tabela K[][] de baixo para cima
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif itens[i-1]["peso"] <= w:
                    K[i][w] = max(itens[i-1]["valor"] + K[i-1][w - itens[i-1]["peso"]], K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]

        # O valor máximo otimizado encontrado fica na última célula
        valor_otimizado = K[n][W]

        # Descobrindo quais itens foram selecionados (Caminho de volta na matriz)
        itens_escolhidos = []
        res_w = W
        for i in range(n, 0, -1):
            if K[i][res_w] != K[i-1][res_w]:
                item_selecionado = itens[i-1]
                itens_escolhidos.append(item_selecionado)
                res_w -= item_selecionado["peso"]

        # Inverte a lista para ficar na ordem original de inserção
        itens_escolhidos.reverse()

        print("====== RESULTADO DO CÁLCULO OTIMIZADO ======")
        print(f"Valor Total Otimizado obtido: R$ {valor_otimizado:.2f}")
        print(f"Itens que couberam sem estourar o limite: {itens_escolhidos}")
        print("============================================\n")

        return {
            "valor_otimizado": float(valor_otimizado),
            "itens_escolhidos": itens_escolhidos
        }
        
    except Exception as e:
        print(f"Erro interno no cálculo matemático: {e}")
        return {"valor_otimizado": 0.0, "itens_escolhidos": []}

# ========================================================
# 2. FUNÇÃO DE CADASTRO CORRIGIDA (SIMULAÇÃO DE REPETIDOS)
# ========================================================

@eel.expose
def cadastrar_transportadora(dados):
    print("\n====== DADOS RECEBIDOS DO CADASTRO ======")
    print(dados)
    print("==========================================\n")
    
    try:
        cnpj = dados.get("cnpj")
        
        # Correção temporária para o erro do console: 
        # Varre a nossa lista local em memória enquanto você não implementa o banco de dados na Controller
        if cnpj in cnpjs_cadastrados_no_sistema:
            print(f"[AVISO] Cadastro negado: O CNPJ {cnpj} já existe no sistema.")
            return {"status": "duplicado"}

        # Adiciona o CNPJ na lista para bloquear caso tente enviar de novo
        cnpjs_cadastrados_no_sistema.append(cnpj)

        print("Cadastro processado e simulado com sucesso!")
        return {"status": "sucesso"}

    except Exception as e:
        print(f"Erro no fluxo de cadastro do backend: {e}")
        return {"status": "erro", "mensagem": str(e)}

# ========================================================
# 3. FUNÇÃO DE LOGIN (EEL)
# ========================================================

@eel.expose
def verificar_login(email, senha):
    print(f"\n====== TENTATIVA DE LOGIN ======")
    print(f"E-mail: {email}")
    print(f"Senha: {senha}")
    print("=================================\n")
    
    try:
        if email == "pimenteltransporte@gmail.com" and senha == "12345678":
            print("Login autorizado!")
            return True
        
        print("Login negado: Usuário ou senha inválidos.")
        return False
        
    except Exception as e:
        print(f"Erro no processo de login: {e}")
        return False

# ========================================================
# INICIALIZAÇÃO DO SISTEMA
# ========================================================

def iniciar_sistema():
    eel.init('web/html')
    print("Sistema Iniciado com sucesso! Abrindo a tela de login...")
    eel.start('login.html', mode='default', size=(1100, 780))

if __name__ == "__main__":
    iniciar_sistema()