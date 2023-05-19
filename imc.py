#Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2). Ao final, escreva se a pessoa está com 

#peso normal #(IMC abaixo de 25), obeso #(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def main():
    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em kg: "))
    imc = peso/altura**2
    situacao = verificar_situacao(imc)

def verificar_situacao(imc):
    if imc>30:
        print(f"Seu imc é de: {imc} e sua situação é de OBESIDADE MÓRBIDA!")
    elif imc>25 and imc<30:
        print(f"Seu imc é de: {imc} e sua situação é de OBESIDADE!")           
    elif imc<25:
        print(f"Seu imc é de: {imc} e sua situação é de PESO NORMAL!")
    

   














main()