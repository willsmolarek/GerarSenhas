import random
import string

complexidade_baixa = string.ascii_lowercase
complexidade_media = string.ascii_letters + string.digits
complexidade_alta = string.ascii_letters + string.digits + string.punctuation

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

tamanho = int(input("Qual o tamanho da senha? "))
complexidade = input("Qual a complexidade da senha (baixa, media ou alta)? ")

senha = gerar_senha(tamanho, complexidade)
print("Sua senha é:", senha)
