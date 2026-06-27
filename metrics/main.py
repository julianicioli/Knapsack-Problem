import sys
sys.path.append("/")
import json
import pandas as pd
from models.mochila_model import MochilaModel
from metrics import executar_medicao
from graph_generator import gerar_graficos

resultados = []
mochila_model = MochilaModel()

casos_teste = [
    {
        "capacidade": 5.0,
        "itens": [
            {'peso': 1, 'valor': 5},
            {'peso': 2, 'valor': 4},
            {'peso': 4, 'valor': 8},
            {'peso': 5, 'valor': 6}
        ]
    },
    {
        "capacidade": 0.0,
        "itens": [{'peso': 2, 'valor': 10}]
    }
]

for caso_teste in casos_teste:
    print("Caso de teste:", caso_teste)
    resultado = executar_medicao(mochila_model, caso_teste["capacidade"], caso_teste["itens"])
    resultados.append(resultado)

df = pd.DataFrame(resultados)

df.to_csv("/metrics/output/metrics.csv", index=False)

resumo = {
    "total_casos_testados": len(casos_teste),
    "capacidade_media": round(df["capacidade"].mean(), 4),
    "num_itens_disponiveis_medio": round(df["num_itens_disponiveis"].mean(), 2),
    "num_itens_selecionados_medio": round(df["num_itens_selecionados"].mean(), 2),
    "peso_total_usado_medio": round(df["peso_total_usado"].mean(), 4),
    "valor_total_medio": round(df["valor_total"].mean(), 4),
    "eficiencia_media": round(df["eficiencia"].mean(), 4),
    "tempo_medio_ms": round(df["tempo_ms"].mean(), 4),
    "memoria_media_mb": round(df["memoria_mb"].mean(), 4),
}

with open("/metrics/output/metrics.json", "w") as arquivo:
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
print("- tempo_x_itens.png")
print("- eficiencia_x_capacidade.png")

print("\nExecução concluída.")