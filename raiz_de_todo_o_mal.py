"""
Raiz de todo o mal foi uma brincadeira na tentativa de achar a raiz quadrada de 666,
mas também serve para a raiz de qualquer número, basta comentar o número 666 e descomentar
a parte de baixo que o script permite o input de números.
"""
n = 0
count = True
numero = 666
# numero = input("Digite um número: \n")
# if (numero.isdigit()):
#     numero = float(numero)
while count:
    if ((n * n != numero) and (n * n < numero)):
        n += 0.0001
        # r = n * n
        # print(f"{n} * {n} = {r}")
        
    else:
        print(f"A raiz quadrada de {numero} é aproximadamente {n}")
        count = False