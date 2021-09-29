"""
Calcular a porcentagem escolhida de um dado número
"""
print("Cálculo de porcentagem")
n = input("Digite o número base: \n")
if (n.isdigit()):
    n = int(n)
p = input("Digite a porcentagem desejada: \n")
if (p.isdigit()):
    p = int(p)

resultado = (n * p) / 100

print(f"O resultado de {p}% de {n} é {resultado}.")