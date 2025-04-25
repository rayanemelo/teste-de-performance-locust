import pandas as pd
import matplotlib.pyplot as plt

# Gera análise do stats.csv
def analisar_stats(path_csv, titulo):
    df = pd.read_csv(path_csv)
    df_endpoints = df[df["Name"] != "Aggregated"]

    df_endpoints["95%"] = pd.to_numeric(df_endpoints["95%"], errors="coerce")
    df_endpoints["Failure Count"] = pd.to_numeric(df_endpoints["Failure Count"], errors="coerce")

    # Métricas médias
    p90 = df_endpoints["90%"].mean()
    p95 = df_endpoints["95%"].mean()
    throughput = df["Requests/s"].mean()

    total_falhas = df_endpoints["Failure Count"].sum()

    # Detecta gargalos: falha ou p95 > 1000ms
    gargalos = df_endpoints[
        (df_endpoints["95%"] > 1000) | (df_endpoints["Failure Count"] > 0)
    ][["Name", "95%", "Failure Count"]]

    relatorio = f"""
📊 Análise - {titulo}
➡️ Tempo médio p90: {p90:.2f} ms
➡️ Tempo médio p95: {p95:.2f} ms
➡️ Throughput médio: {throughput:.2f} req/s
❌ Total de falhas: {int(total_falhas)}

🔥 Endpoints com gargalo (p95 > 1000ms ou falhas):
"""

    if not gargalos.empty:
        for _, row in gargalos.iterrows():
            relatorio += f"   - {row['Name']}: p95 = {row['95%']} ms | falhas = {int(row['Failure Count'])}\n"
    else:
        relatorio += "   - Nenhum gargalo identificado\n"

    print(relatorio)
    return throughput, p95, relatorio


usuarios = [10, 50, 100, 500]
throughputs = []
p95s = []
relatorios = []

# Primeiro: gera os dados
for u in usuarios:
    arquivo = f"resultado_{u}_users_stats.csv"
    t, p, relatorio = analisar_stats(arquivo, f"{u} usuários")
    throughputs.append(t)
    p95s.append(p)
    relatorios.append(relatorio)

# Depois: gera e salva o gráfico
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(usuarios, throughputs, marker='o', label="Throughput (req/s)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Requisições por segundo")
plt.title("Throughput vs Usuários")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(usuarios, p95s, marker='o', color="red", label="P95 (ms)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Tempo de resposta P95 (ms)")
plt.title("Tempo de resposta P95 vs Usuários")
plt.grid(True)

plt.tight_layout()
plt.savefig("analise_graficos.png", format='png')
print("Gráficos salvos como: analise_graficos.png")
plt.show()

# Gera relatório final
with open("relatorio_final.txt", "w", encoding="utf-8") as f:
    f.write("📄 RELATÓRIO FINAL DE PERFORMANCE\n")
    f.write("="*40 + "\n\n")
    for r in relatorios:
        f.write(r)
        f.write("\n" + "-"*40 + "\n")

print("Relatório salvo como: relatorio_final.txt")
