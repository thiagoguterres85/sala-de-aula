# Exercicio 1
def fizz_buzz (numero:int):
    if numero % 3 == 0 and % 5 == 0:
          return "fizzbuzz"
   
    elif numero % 5 == 0:
          return "fizz"
    
    elif numero  % 3 == 0:
          return "buzz"
    else:
          return numero 
    if __name__ == '__main__':
       
    
        print (fizz_buzz)



# Exercicio 2
def verificar_maioridade(idade:int):
    if idade >18:  
        return "Maior de Idade" 

    else:
        return "Menor de Idade"
    if __name__ == '__main__':
       
        print (verificar_maioridade)



#Exercicio 3 
def classificar_numero (numero:int):
     if numero > 0: 
          return "Positivo"
     if numero < 0: 
          return "Negativo"
if __name__ == '__main__':

    print (classificar_numero)



#Exercicio 4
def calcular_resultado (nota1:int, nota2:int):
     if nota1 > 7.0:
          return "Aprovado"
     else: 
          return "Reprovado"
     if __name__ == '__main__':
         
         print (calcular_resultado)


#Exercicio 5 
def maior_de_dois (a:int, b:int):
     if a > b:
          return "o primeiro é maior"
     if b < a:
          return "o segundo é maior"
     else: 
          return "são iguais"   
     
     if __name__ == '__main__':
          print (maior_de_dois)
         






#Exercicio 6 (medio)
def calcular_desconto (valor_compra:float, e_cliente_vip:bool):


    if e_cliente_vip or valor_compra > 200:
          return f"Valor final: R$ {valor_compra*0.85}"
    
    return f"Valor final: R$ {valor_compra * 0.95}" 
    
    if __name__ == '__main__':
         

         
    
      