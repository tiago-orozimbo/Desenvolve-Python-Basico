def validador_senha(senha):
    # Critérios de validação
    comprimento_valido = len(senha) >= 8
    letra_maiuscula = any(char.isupper() for char in senha)
    letra_minuscula = any(char.islower() for char in senha)
    numero = any(char.isdigit() for char in senha)
    caractere_especial = any(char in '@#$%^&*()_+=-`~[]{}|\\;:"\',.<>?/!' for char in senha)
    return comprimento_valido and letra_maiuscula and letra_minuscula and numero and caractere_especial

senha1 = input('Digite sua senha: ')
senha2 = input('Digite sua senha: ')
senha3 = input('Digite sua senha: ')
print(validador_senha(senha1))  
print(validador_senha(senha2))  
print(validador_senha(senha3))  
