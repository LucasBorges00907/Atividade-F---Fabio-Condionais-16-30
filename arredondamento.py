#Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
#maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
#contrario, é arredondado para o inteiro imediatamente inferior.

def main():
    numero = float(input("Digite o valor que quer arredondar: "))
    numero_arredondado = arrendondar(numero)

    print(f"O número {numero} arredondado fica {numero_arredondado}")

def arrendondar(numero): 

    resto = numero - int(numero)
    if resto >= 0.5:
        numero = int(numero) + 1
        return numero
    else:
        numero = int(numero)
        return numero









main()