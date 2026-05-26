# exercicio_dia2.py - Dia 2 (26/05/2026)

print("=== Dia 2 - Python Intermediário ===\n")

# Exercício 1: Condicionais (if, elif, else)
gasto = 450

if gasto > 300:
    print("Alerta: Gastos altos este mês!")
elif gasto > 150:
    print("Gastos moderados.")
else:
    print("Gastos controlados.")

print("-" * 5)

# Exercício 2: Função + Loop
def categorizar_gasto(valor):
    if valor > 200:
        return "Alto"
    elif valor > 50:
        return "Médio"
    else:
        return "Baixo"

gastos = [89.90, 245.50, 45.00, 320.00]

for g in gastos:
    print(f"Gasto R$ {g:.2f} → Categoria: {categorizar_gasto(g)}")

produtos = ['maçã', 'banana', 'laranja']

for fruta in produtos:
    print(f'Processando a fruta: {fruta}') # Instrução 1
    fruta_maiuscula = fruta.upper()       # Instrução 2
print(f'Nome formatado: {fruta_maiuscula}') # Instrução 3

print("\n✅ Dia 2 concluído com sucesso!")