# Função para inverter os caracteres de uma string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):  # Percorre a string de trás para frente
        string_invertida += s[i]  # Adiciona cada caractere à nova string
    return string_invertida

# Entrada do usuário ou string pré-definida
entrada_usuario = input("Informe uma string para inverter (ou pressione Enter para usar a padrão): ")
if entrada_usuario.strip() == "":
    entrada_usuario = "Hello, World!"  # String padrão.

# Inverter a string
resultado = inverter_string(entrada_usuario)

# Exibir o resultado
print(f"String invertida: {resultado}")
