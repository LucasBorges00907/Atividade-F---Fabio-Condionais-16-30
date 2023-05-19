#Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
#um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
#não pode ser negativo.

def main():
    x1 = float(input('Primeiro vértice:\nx = '))
    y1 = float(input('y = '))
    
   
    x2 = float(input('\nVértice oposto:\nx = ')) 
    y2 = float(input('y = '))
    
    area = calcular_area(x1, x2, y1, y2)
    
    print(f'A area do retângulo é {area}.')

def calcular_area(x1, x2, y1, y2):
    ladox = x2 - x1
    ladoy = y2 - y1
    
    area = ladox * ladoy
    if area > 0:
        return area
    elif area < 0:
        area = (-1) * area
        return area
    else:
        return 'nula'
      
    
main()