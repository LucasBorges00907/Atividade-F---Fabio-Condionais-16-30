#Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
#uma mensagem de permissão de acesso ou não.

def main():
    senha = int(input('Digite a senha:\n     '))
    
    if senha == 1234:
        print('ACESSO LIBERADO!')
    
    else:
        print('ACESSO NEGADO!')
        main()


main()