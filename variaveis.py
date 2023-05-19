#Escreva um algoritmo para ler um número e verificar se ele obedece a esta característica.
#17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for
#1
#escreva a soma dessas variáveis mais o resto da divisão;

#se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; 
#se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual 
#a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

def main():
    numero1 = int(input("Digite o valor 1: "))
    numero2 = int(input("Digite o valor 2: "))

    fazer_operacoes(numero1,numero2)

def fazer_operacoes(numero1,numero2):
    resto = numero1%numero2
    if resto == 1:
        resultado = numero1+numero2+resto
        print (f">>>{resultado}<<<")
    elif resto == 2:
        if numero1%2 == 0:
            print("O número 1 é par")
        else:
            print("O número 1 é ímpar")
        if numero2%2 == 0:
            print("O número 2 é par")
        else:
            print("O número 2 é ímpar")
    elif resto == 3:
        resultado = (numero1+numero2)*numero1
        print (f">>>{resultado}<<<")
    elif resto == 4:
        if numero2!=0:
            resultado = (numero1+numero2)/numero2
            print (f">>>{resultado}<<<")
    else:
        quadradonum1 = numero1*numero1
        quadradronum2 = numero2*numero2
        print(f"Quadrado numero 1: {quadradonum1}")
        print(f"Quadrado numero 2: {quadradronum2}")

        
        
        


        








main()