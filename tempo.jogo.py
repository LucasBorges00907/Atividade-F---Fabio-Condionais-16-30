#Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
#hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
#máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
#seguinte.

def main():
    horas_inicio = int(input('Qual o horário de início do jogo? (HH:MM)\nHoras:'))
    minutos_inicio = int(input('Minutos: '))
        
    horas_fim = int(input('Qual o horário do fim do jogo? (HH:MM)\nHoras:'))
    minutos_fim = int(input('Minutos: '))
    
    
    duracao_jogo = calcular_duracao(horas_inicio, horas_fim, minutos_inicio, minutos_fim)
    
    print(f'A partida durou {duracao_jogo}')
    
    
def calcular_duracao(horas_inicio, horas_fim, minutos_inicio, minutos_fim):
    tempo_inicio = horas_inicio * 60 + minutos_inicio
    
    tempo_fim = horas_fim * 60 + minutos_fim
    
    if tempo_fim < tempo_inicio:
        duracao = 24 * 60 - tempo_inicio + tempo_fim
        return f'{duracao // 60}:{duracao % 60}.'
    elif tempo_inicio < tempo_fim:
        duracao = tempo_fim - tempo_inicio
        return f'{duracao // 60}:{duracao % 60}.'


main()