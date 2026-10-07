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



#Exercicio 4
def zerar_negativos(numeros:list):
    aux = []

    for numero in numeros:
        if numero < 0:
           aux.append(0)
        else:
            aux.append(numero)  

    return aux

if __name__ == '__main__':

    aux = zerar_negativos([4, -2, 7, -9, 0])

    print(aux) 

 
         

#Exercicio 5
def contem_valor (lista:list, alvo):
    index = 0
    while(index < len(lista)):
        if lista[index] == alvo:
            return True 
        index=+1

if __name__ == '__main__':
 print(contem_valor(["maçã", "banana", "uva"], "banana"))     



#Exercicio 6
def contar_aprovados(notas:int):
    count = 0
    for nota in notas:
        if nota >= 7.0:
         count+=1 
        
    return count 

if __name__ == '__main__':
   print(contar_aprovados([8.5, 5.0, 7.0, 6.5, 9.0]))