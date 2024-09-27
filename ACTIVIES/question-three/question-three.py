# Lista que contém o faturamento diário (exemplo)
from jsontt import faturamento_diario

def calcular_faturamento(faturamento):
    # Cria uma lista para armazenar valores de faturamento válidos (maiores que zero)
    faturamentoValido = []
    
    # Filtra os valores de faturamento, adicionando apenas os que são maiores que zero
    for item in faturamento:
        if item['valor'] > 0:
            faturamentoValido.append(item['valor'])

    # Calcula o menor e maior valor de faturamento
    menorValor = min(faturamentoValido)
    maiorValor = max(faturamentoValido)
    
    # Calcula a média dos valores de faturamento válidos
    media = sum(faturamentoValido) / len(faturamentoValido)

    # Conta quantos dias têm faturamento acima da média.
    dias_Acima_media = 0
    for valor in faturamentoValido:
        if valor > media:
            dias_Acima_media += 1

    return menorValor, maiorValor, dias_Acima_media

# Chama a função calcular_faturamento com a lista de faturamento diário e armazena os resultados
menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

# Imprime os resultados
print(f'Menor valor faturamento: {menor:.2f}')
print(f'Maior valor faturamento: {maior:.2f}')
print(f'Números de dia com faturamento acima da média: {dias_acima}')