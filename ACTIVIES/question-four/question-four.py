from jsonEstados import estados

def calcular_porcentagem(parte, total):
    # Função que calcula a porcentagem de 'parte' em relação a 'total'.
    if total == 0:
        return 0  # Retorna 0% se o total for zero para evitar divisão por zero.
    return (parte / total) * 100  # Retorna a porcentagem calculada.

# Calcula o total de contribuição somando os faturamentos de todos os estados.
total_contribuicao = estados[0]['Faturamento'] + estados[1]['Faturamento'] + estados[2]['Faturamento'] + estados[3]['Faturamento'] + estados[4]['Faturamento']

# Calcula a contribuição percentual de cada estado em relação ao total de contribuição.
contribuicao_SaoPaulo = calcular_porcentagem(estados[0]['Faturamento'], total_contribuicao)
contribuicao_RioDeJaneiro = calcular_porcentagem(estados[1]['Faturamento'], total_contribuicao)
contribuicao_MinasGerais = calcular_porcentagem(estados[2]['Faturamento'], total_contribuicao)
contribuicao_EspiritoSanto = calcular_porcentagem(estados[3]['Faturamento'], total_contribuicao)
contribuicao_outrosEstados = calcular_porcentagem(estados[4]['Faturamento'], total_contribuicao)

# Imprime a contribuição percentual de cada estado
print(f'A contribuição do estado de São Paulo foi de %{contribuicao_SaoPaulo:.2f}')
print(f'A contribuição do estado do Rio de Janeiro foi de %{contribuicao_RioDeJaneiro:.2f}')
print(f'A contribuição do estado de Minas Gerais foi de %{contribuicao_MinasGerais:.2f}')
print(f'A contribuição do estado do Espírito Santo foi de %{contribuicao_EspiritoSanto:.2f}')
print(f'A contribuição dos outros estados foi de %{contribuicao_outrosEstados:.2f}')