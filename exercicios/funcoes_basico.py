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


#Exercicio 5
def resumo_circulo (raio: float):
    pi = 3.14159
    area = pi * (raio**2)
    return f"Um circulo de raio {raio} tem área de {area:.2f}"

if __name__ == '__main__':
    print(resumo_circulo(3.0))