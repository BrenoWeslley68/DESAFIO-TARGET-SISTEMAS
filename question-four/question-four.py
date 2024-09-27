from jsonEstados import estados

def calcular_porcentagem(parte,total):
    if total == 0:
        return 0
    return (parte/total) * 100

total_contribuicao = estados[0]['Faturamento'] + estados[1]['Faturamento'] + estados[2]['Faturamento'] + estados[3]['Faturamento'] + estados[4]['Faturamento']


contribuicao_SaoPaulo = calcular_porcentagem(estados[0]['Faturamento'], total_contribuicao)
contribuicao_RioDeJaneiro = calcular_porcentagem(estados[1]['Faturamento'], total_contribuicao)
contribuicao_MinasGerais = calcular_porcentagem(estados[2]['Faturamento'], total_contribuicao)
contribuicao_EspiritoSanto = calcular_porcentagem(estados[3]['Faturamento'], total_contribuicao)
contribuicao_outrosEstados = calcular_porcentagem(estados[4]['Faturamento'], total_contribuicao)


print(f'A contribuição do estado de São Paulo foi de %{contribuicao_SaoPaulo}')
print(f'A contribuição do estado do Rio de Janeiro foi de %{contribuicao_RioDeJaneiro}')
print(f'A contribuiçao do estado de Minas Gerais foi de %{contribuicao_MinasGerais}')
print(f'A contribuiçao do estado do Espírito Santo foi de %{contribuicao_EspiritoSanto}')
print(f'A contribuição dos outros estados foi de %{contribuicao_outrosEstados}')