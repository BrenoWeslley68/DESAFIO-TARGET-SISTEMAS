# Função que gera a sequência de Fibonacci até o número informado
def fibonacci(num):
    # Inicializa a lista com os dois primeiros números da sequência de Fibonacci
    fib = [0, 1]

    # Gera a sequência de Fibonacci enquanto o último número for menor que o número informado
    while fib[-1] < num:
        # Adiciona o próximo número da sequência à lista
        fib.append(fib[-1] + fib[-2])
    return fib

# Função que verifica se o número informado pertence à sequência de Fibonacci
def verifica(num):
    # Chama a função fibonacci para gerar a sequência até o número informado
    sequencia = fibonacci(num)

    # Verifica se o número está na sequência gerada
    if num in sequencia:
        print(f'O número {num} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {num} não pertence à sequência de Fibonacci.')

# Número a ser verificado
numero = int(input('Informe um número: '))

# Chama a função verifica e exibe o resultado
print(verifica(numero))