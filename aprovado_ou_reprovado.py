#Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.

def main():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1+nota2)/2

    verificar_situacao(media)

def verificar_situacao(media):
    if media>=7:
        print("Aprovado")
    else:
        print("Você ficou de Prova Final")
        notaprovafinal = float(input("Digite a nota da prova final: "))
        notafinal = (notaprovafinal+media)/2
        if notafinal>=5:
            print("Aprovado")
        else:
            print("Reprovado")
        




main()