def formatar_saudacao (nome: str , cidade:str):
    return f"Ola {nome}, seja bem-vindo(a) a {cidade}!"





# Exercicio2 
def calcular_perimetro (largura:float, altura:float):   
    perimetro = 2* (largura + altura)  
    return   perimetro  


    


# Exercicio3
def fahrenheit_para_celsius (temp_f: str):
    temp_celsius = (temp_f - 32) * (5 / 9) 
    return temp_celsius 

    


#Exercio 4
def calcular_gorjeta_por_pessoa (conta:float, porcentagem_gorjeta:float, pessoas:int):
    gorjeta = (conta* (porcentagem_gorjeta / 100)) / pessoas 
    return gorjeta 

if __name__ == '__main__':
    gorjeta = calcular_gorjeta_por_pessoa(100, 15, 3)
    print (gorjeta)