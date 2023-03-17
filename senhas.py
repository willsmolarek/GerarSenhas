import random
import string

# Define as opções de caracteres para cada nível de complexidade
complexidade_baixa = string.ascii_lowercase
complexidade_media = string.ascii_letters + string.digits
complexidade_alta = string.ascii_letters + string.digits + string.punctuation

# Define a função que gera a senha aleatória
def gerar_senha(tamanho, complexidade):
    caracteres = ""
    if complexidade == "baixa":
        caracteres = complexidade_baixa
    elif complexidade == "media":
        caracteres = complexidade_media
    elif complexidade == "alta":
        caracteres = complexidade_alta
    else:
        print("Complexidade inválida.")
        return ""
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Pede ao usuário o tamanho e a complexidade da senha
tamanho = int(input("Qual o tamanho da senha? "))
complexidade = input("Qual a complexidade da senha (baixa, media ou alta)? ")

# Gera a senha e imprime na tela
senha = gerar_senha(tamanho, complexidade)
print("Sua senha é:", senha)
