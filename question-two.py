#Função que gera a sequência de Fibonacci até o número informado
def fibonacci(num):
    fib = [0,1]

    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib

# Função que verifica se o número informado pertence à sequência de Fibonacci
def verifica(num):
    sequencia = fibonacci(num)

    if num in sequencia:
        print(f'O número {num} pertence a sequencia de fibonacci.')
    else:
        print(f'O número {num} não pertence a sequencia de fibonacci')

# Número a ser verificado
numero = int(input('Informe um número: '))

# Chama a função e exibe o resultado
print(verifica(numero))