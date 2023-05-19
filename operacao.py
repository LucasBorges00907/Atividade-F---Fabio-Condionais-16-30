def main():
    numero1 = int(input('Digite o valor 1: '))
    numero2 = int(input('Digite o valor 2: '))
    
    print('Sabendo que:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
    operacao = int(input('Digite o valor correspondete à operação desejada:\n>>> ' ))
    
    resultado = calcular(numero1, numero2, operacao)
    
    print(f'O resultado da operação selecionada é {resultado}')
    

def calcular(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
        return resultado
    elif operacao == 2:
        resultado = num1 - num2
        return resultado
    elif operacao == 3:
        resultado = num1 * num2
        return resultado
    elif operacao == 4:
        resultado = num1 / num2
        return resultado


main()