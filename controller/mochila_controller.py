import eel
from models.mochila_model import MochilaModel

class MochilaController:
    def __init__(self):
        self.model = MochilaModel()

    def processar_otimizacao(self, transporte, itens):
        # Pega a capacidade máxima informada na tela de transporte
        capacidade_maxima = float(transporte['capacidade'])
        
        # 1. Roda o algoritmo da mochila (Regra de Negócio que está no Model)
        valor_total, itens_selecionados = self.model.resolver_knapsack(capacidade_maxima, itens)
        
        # 2. Salva no banco de dados se houver itens selecionados
        sucesso_banco = False
        if itens_selecionados:
            sucesso_banco = self.model.salvar_no_banco(transporte, itens_selecionados)
            
        # 3. Retorna o resultado estruturado para o Eel devolver ao JS
        return {
            "sucesso": sucesso_banco,
            "valor_total": valor_total,
            "itens_escolhidos": itens_selecionados
        }

# O decorator @eel.expose fica aqui na função global.
# É esta função que o seu script.js vai chamar assim: eel.otimizar_e_salvar(transporte, itens)
@eel.expose
def otimizar_e_salvar(transporte, itens):
    # Criamos a instância do controlador para rodar a lógica MVC
    controlador = MochilaController()
    return controlador.processar_otimizacao(transporte, itens)