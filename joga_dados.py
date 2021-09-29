"""
O joga_dados foi criado com a intenção de tentar visualizar quantas vezes cada face do d6
tem a possibilidade de aparecer. Primeiro foi usada a biblioteca random uma vez escolhendo
entre 1 e 6. Depois percebi que se usar mais de um random por jogada do dado e tirar a média
dos resultados torna mais difícil de sair o 6, que é a forma atual do script. Por fim foi adicionada
uma função de soma ao script pra somar as faces do dado que apareceram.
"""
# Biblioteca random gera números aleatórios
import random

# Um array de resultados com 6 posições, uma para cada face do dado (d6).
# Cada vez que uma face do dado aparece é somado 1 a sua posição correspondente
results = [0,0,0,0,0,0]

# O usuário digita um número, que é checado para confirmar que é um número e não letras
iterations = input("Número de vezes a jogar o dado: ")
if (iterations.isdigit()):
    iterations = int(iterations)
iterations_control = iterations

# Função que calcula a soma de todas as faces do dado de acordo com as vezes que apareceram
def soma(array):
    face_dos_dados = [1,2,3,4,5,6]
    pos = 0
    soma = 0
    for a in array:
        soma += array[pos] * face_dos_dados[pos]
        pos += 1
    return soma

# A função frase escreve no console quantas vezes cada face do dado apareceu nos resultados
def frase(array):
    num = 1
    for obj in array:
        print(f"O número {num} apareceu {obj} vezes.")
        num += 1

while (iterations > 0):
    # Cada vez que o loop é executado um dado é jogado e guardamos o resultado, ao mesmo tempo
    # subtrai-se 1 do número do usuário até que chegue em 0
    iterations -= 1

    # Tirando a média de dois ou mais números faz com que o 1 e o 6 apareçam menos vezes
    # Iniciando um array de controle que vai receber números aleatórios para cada zero que tiver
    random_numbers = [0,0,0]
    # random_numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # quanto mais números menos chances de dar 1, 5 ou 6
    
    # Iniciando duas varáveis de controle
    # Dado vai receber a média dos números aleatórios salvos no array de controle
    dado = 0
    # X vai marcar a posição atual do array de controle para salvar os números gerados
    x = 0

    # Para cada zero no array de controle um número aleatório será gerado e guardado
    for number in random_numbers:
        number = int(random.randint(0,5)+1) # gerando um número aleatório entre 1 e 6
        random_numbers[x] = number
        dado += number
        x += 1

    # A média dos números
    dado = int(dado / len(random_numbers))
    #dado = int(random.randint(1,6)) # usando random direto dá resultados muito aproximados

    # Com o resultado da média, subtrai 1 para pegar a posição da face do dado no array de resultado,
    # onde 0 representa a face 1 do dado, 1 representa a face 2 e assim por diante, depois é somado
    # 1 para a posição referente ao resultado para sabermos quantas vezes aquela face apareceu
    pos = dado - 1
    results[pos] += 1
    # print(f"Números aleatórios: {random_numbers}. Média: {dado}")

# Aqui retornamos o valor que o usuário digitou e chamamos a função que escreve o resultado
# de quantas vezes cada face do dado apareceu.
print(f"O dado foi jogado {iterations_control} vezes.")
frase(results)
print(f"A soma dos dados é {soma(results)}")