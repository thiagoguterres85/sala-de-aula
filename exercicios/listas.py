def filtrar_pares (numeros:list): 
    pares = []

    for numero in numeros:
        if numero %2==0:  
            pares.append(numero)
        
    return pares
    
       

    



#Exercicio 2 
def contar_negativos (numeros: list):
    count = 0
    for numero in numeros:
         if numero < 0:
             count+=1
     
    return "negativos"


    


#Exercicio 3 
def somar_maiores_que (numeros:list, limite:int):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma+=numero
    return soma 
              

    soma = somar_maiores_que ([10, 5, 20, 3, 15], 8)

    print(soma)


#Exercicio 4
def zerar_negativos (numeros:list):
    for numero in numeros:
        if numero < 0: 
    
            return negativados 
        
if __name__ == '__main__':
    negativados = zerar_negativos ([4, -2, 7, -9, 0])
        
    print (negativados) 



 
         

