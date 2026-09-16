def formatar_saudacao (nome: str , cidade:str):
    return f"Ola {nome}, seja bem-vindo(a) a {cidade}!"

if __name__ == '__main__':

    saudacao = formatar_saudacao ("Alice", "Porto Alegre")

print(saudacao)


# Exercicio2 
def calcular_perimetro (largura:float, altura:float):   
    return 2* (5.0 + 10.0)
    calcular = calcular_perimetro (2* 5.0 + 10.0)

    print (calcular)