# exercicio_dia3.py - Dia 3

print("=== Dia 3 - Consolidando Python Intermediário ===\n")

# 1. Listas e Dicionários
gastos = [
    {"descricao": "ifood", "valor": 89.90, "categoria": "alimentacao"},
    {"descricao": "Shell", "valor": 245.50, "categoria": "combustivel"},
    {"descricao": "Netflix", "valor": 45.90, "categoria": "assinatura"},
    {"descricao": "Supermercado", "valor": 320.00, "categoria": "alimentacao"}
]

# Somar gastos por categoria
total_por_categoria = {}
for gasto in gastos:
    cat = gasto["categoria"]
    total_por_categoria[cat] = total_por_categoria.get(cat, 0) + gasto["valor"]

print("Total por categoria:")
for cat, valor in total_por_categoria.items():
    print(f"{cat.capitalize()}: R$ {valor:.2f}")

# 2. Lambda + Filter + Map
valores = [89.90, 245.50, 45.90, 320.00, 15.00]

# Filtrar gastos acima de 100
altos = list(filter(lambda x: x > 100, valores))
print(f"\nGastos altos: {altos}")

# Dobrar todos os valores
dobrados = list(map(lambda x: x * 2, valores))
print(f"Valores dobrados: {dobrados}")

numeros = {1, 2, 3, 3, 2}
print(numeros)


print("\nDia 3 concluído com sucesso!")