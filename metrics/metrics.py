import time
import psutil
import os


def executar_medicao(mochila_model, capacidade, itens):
    processo = psutil.Process(os.getpid())
    memoria_antes = processo.memory_info().rss / 1024 / 1024

    inicio = time.perf_counter()
    valor_total, itens_selecionados = mochila_model.resolver_knapsack(capacidade, itens)
    fim = time.perf_counter()

    memoria_depois = processo.memory_info().rss / 1024 / 1024

    peso_total_usado = sum(item["peso"] for item in itens_selecionados)
    valor_total_obtido = valor_total
    num_itens_disponiveis = len(itens)
    num_itens_selecionados = len(itens_selecionados)

    # Evita divisão por zero caso capacidade usada seja 0
    eficiencia = round(valor_total_obtido / peso_total_usado, 6) if peso_total_usado > 0 else 0.0

    return {
        "capacidade": capacidade,
        "num_itens_disponiveis": num_itens_disponiveis,
        "num_itens_selecionados": num_itens_selecionados,
        "peso_total_usado": round(peso_total_usado, 6),
        "valor_total": round(valor_total_obtido, 6),
        "eficiencia": eficiencia,
        "tempo_ms": round((fim - inicio) * 1000, 6),
        "memoria_mb": round(memoria_depois - memoria_antes, 6),
    }