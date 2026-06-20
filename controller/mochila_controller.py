import eel
from models.mochila_model import MochilaModel

class MochilaController:
    def __init__(self):
        self.model = MochilaModel()

# O decorator @eel.expose torna essa função visível dentro do seu arquivo script.js
@eel.expose
def otimizar_e_salvar(transporte, itens):
    model = MochilaModel()
    
    # Pega a capacidade máxima informada na tela de transporte
    capacidade_maxima = float(transporte['capacidade'])
    
    # 1. Roda o algoritmo da mochila (Regra de Negócio)
    valor_total, itens_selecionados = model.resolver_knapsack(capacidade_maxima, itens)
    
    # 2. Salva no banco de dados se houver itens selecionados
    sucesso_banco = False
    if itens_selecionados:
        sucesso_banco = model.salvar_no_banco(transporte, itens_selecionados)
        
    # 3. Retorna um dicionário contendo os dados processados para o JavaScript usar na tela
    return {
        "sucesso": sucesso_banco,
        "valor_total": valor_total,
        "itens_escolhidos": itens_selecionados
    }