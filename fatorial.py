"""
Fatorial é uma representação matemática que significa multiplicar um número por todos os números
positivos menores ou iguais a ele, como por exemplo 5! seria 5 * 4 * 3 * 2 * 1. Foi tentado colocar
este pensamento em forma de código para ver se funcionaria. E funcionou.
"""
#Pegamos um número dado pelo usuário, checamos se é um dígito e convertemos para integer
print("Calculadora Fatorial")
n = input("Digite um número: \n")
if (n.isdigit()):
    n = int(n)  

# Diminuímos 1 do número dado para começar a iteração pelos números subsequentes
# que serão guardados no contador. O resultado guardará o estado do número a cada iteração
contador = n - 1 
resultado = n

# Enquanto o contador for maior que zero multiplicaremos o resultado atual pelo contador atual,
# atualizando o resultado e diminuindo 1 do contador
while (contador > 0):
    resultado = resultado * contador
    contador -= 1

print(f"O resultado de {n} fatorial ({n}!) é {resultado}.")