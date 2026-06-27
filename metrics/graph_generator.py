import matplotlib.pyplot as plt


def gerar_graficos(df):

    df = df.sort_values("entrada")

    # Tempo x Entrada

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["entrada"],
        df["tempo_ms"],
        marker="o"
    )

    plt.title("Tempo de Execução x Entrada")

    plt.xlabel("Número Sorteado")

    plt.ylabel("Tempo (ms)")

    plt.grid(True)

    plt.savefig("/app/output/performance_graph.png")

    plt.close()

    # Iterações x Entrada

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["entrada"],
        df["iteracoes"],
        marker="o"
    )

    plt.title("Iterações x Entrada")

    plt.xlabel("Número Sorteado")

    plt.ylabel("Quantidade de Iterações")

    plt.grid(True)

    plt.savefig("/app/output/iterations_graph.png")

    plt.close()