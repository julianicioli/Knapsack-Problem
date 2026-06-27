import random
import json
import pandas as pd

from metrics import executar_medicao
from graph_generator import gerar_graficos

resultados = []

numeros_sorteados = [random.randint(100, 1000) for _ in range(10)]

print("\nNúmeros sorteados:")
print(numeros_sorteados)

for numero in numeros_sorteados:

    resultado = executar_medicao(numero)

    resultados.append(resultado)

df = pd.DataFrame(resultados)

df.to_csv("/app/output/metrics.csv", index=False)

resumo = {
    "numeros_sorteados": numeros_sorteados,
    "tempo_medio_ms": round(df["tempo_ms"].mean(), 4),
    "memoria_media_mb": round(df["memoria_mb"].mean(), 4),
    "iteracoes_media": round(df["iteracoes"].mean(), 2)
}

with open("/app/output/metrics.json", "w") as arquivo:
    json.dump(
    resumo,
    arquivo,
    indent=4,
    ensure_ascii=False
)

print("\nResultados obtidos:")
print(df)

gerar_graficos(df)

print("\nArquivos gerados em /output")
print("- metrics.csv")
print("- metrics.json")
print("- performance_graph.png")
print("- iterations_graph.png")

print("\nExecução concluída.")