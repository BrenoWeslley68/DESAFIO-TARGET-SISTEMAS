# Define um índice máximo para o loop
int_INDICE = 13

# Inicializa a variável soma para armazenar a soma dos números
soma = 0

# Inicializa a variável k que será usada para iterar até int_INDICE
k = 0

# Loop enquanto k for menor que int_INDICE
while k < int_INDICE:
    k += 1              # Incrementa k em 1 a cada iteração.
    soma += k          # Adiciona o valor atual de k à soma
    print(soma, end=' ')  # Imprime o valor atual da soma, sem pular para a próxima linha

# Após o loop, imprime o valor final da soma
print(f'\n O valor final de soma é {soma}')
