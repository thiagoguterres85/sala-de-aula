def filtrar_pares (numeros:list): 
    pares = []

    for numero in numeros:
        if numero %2==0:  
            pares.append(numero)
        
    return pares
    
       
if __name__ == '__main__':
        numeros_pares = filtrar_pares([1, 2, 3, 4, 5, 6])
        
        print (numeros_pares)

