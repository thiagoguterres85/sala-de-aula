def filtrar_pares (numeros:list): 
    pares = []

    for numero in numeros:
        if numero %2==0:  
            pares.append(numero)
        
    return pares
    
       
if __name__ == '__main__':
        numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
        

        print (numeros_pares)



#Exercicio 2 
def contar_negativos (numeros: list):
    count = 0
    for numero in numeros:
         if numero < 0:
             count+=1
     
    return "negativos"

if __name__ == '__main__':
    count = contar_negativos ([10, -3, 0, -5, 8, -1])
    
    print (count)    



 
         

