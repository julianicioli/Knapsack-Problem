import time
import psutil
import os


def eh_primo(numero):

    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


def encontrar_n_esimo_primo(n):

    contador = 0
    numero = 1
    iteracoes = 0

    while contador < n:

        numero += 1
        iteracoes += 1

        if eh_primo(numero):
            contador += 1

    return numero, iteracoes


def executar_medicao(n):

    processo = psutil.Process(os.getpid())

    memoria_antes = processo.memory_info().rss / 1024 / 1024

    inicio = time.perf_counter()

    primo, iteracoes = encontrar_n_esimo_primo(n)

    fim = time.perf_counter()

    memoria_depois = processo.memory_info().rss / 1024 / 1024

    return {
        "entrada": n,
        "primo": primo,
        "tempo_ms": round((fim - inicio) * 1000, 6),
        "memoria_mb": round(memoria_depois - memoria_antes, 6),
        "iteracoes": iteracoes
    }