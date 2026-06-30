import matplotlib.pyplot as plt


def gerar_graficos(df):
    df = df.sort_values("num_itens_disponiveis")

    # Gráfico 1: Tempo x Número de Itens Disponíveis
    plt.figure(figsize=(10, 6))
    plt.plot(
        df["num_itens_disponiveis"],
        df["tempo_ms"],
        marker="o",
        color="steelblue"
    )
    plt.title("Tempo de Execução x Número de Itens Disponíveis")
    plt.xlabel("Número de Itens Disponíveis")
    plt.ylabel("Tempo (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/metrics/output/tempo_x_itens.png")
    plt.close()

    # Gráfico 2: Eficiência x Capacidade da Mochila
    df_sorted_cap = df.sort_values("capacidade")
    plt.figure(figsize=(10, 6))
    plt.plot(
        df_sorted_cap["capacidade"],
        df_sorted_cap["eficiencia"],
        marker="o",
        color="darkorange"
    )
    plt.title("Eficiência (Valor / Peso Usado) x Capacidade da Mochila")
    plt.xlabel("Capacidade da Mochila")
    plt.ylabel("Eficiência (valor / peso usado)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/metrics/output/eficiencia_x_capacidade.png")
    plt.close()