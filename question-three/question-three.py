# Lista que contém o faturamento diário (exemplo)
from jsontt import faturamento_diario

def calcular_faturamento(faturamento):
    faturamentoValido = []
    for item in faturamento:
        if item['valor'] > 0:
            faturamentoValido.append(item['valor'])

    menorValor = min(faturamentoValido)
    maiorValor = max(faturamentoValido)
    media = sum(faturamentoValido) / len(faturamentoValido)

    dias_Acima_media = 0
    for valor in faturamentoValido:
        if valor > media:
            dias_Acima_media += 1

    return menorValor, maiorValor, dias_Acima_media

menor, maior, dias_acima = calcular_faturamento(faturamento_diario)

print(f'Menor valor faturamento: {menor:.2f}')
print(f'Maior valor faturamento: {maior:.2f}')
print(f'Números de dia com faturamento acima da média: {dias_acima}')
