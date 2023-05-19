#Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
#quarto) em que o ângulo se localiza.

def main():

    angulo = int(input("Digite o valor do ângulo (Entre 0 e 360°): "))
    quadrante = verificar_quadrante(angulo)
    print(f"O ângulo {angulo} está no quadrante {quadrante}")

def verificar_quadrante(angulo):
    if angulo<=90:
        quadrante = 1
        return quadrante
    elif angulo>90 and angulo<=180:
        quadrante = 2
        return quadrante
    elif angulo>180 and angulo<=270:
        quadrante = 3
        return quadrante
    elif angulo>270 and angulo<360:
        quadrante = 4
        return quadrante
    else:
        print("O valor é inválido!")

        



main()


