#Treinando If, Elif, Else

'''Criar um programa que dependo da temperatura (em celsius) de um bife ele retona o ponto de cozimento em portugues. O usuario devera fornecer a temperatura.

Temperatura - Cozimento
48°C - Selada
53°C - Ao ponto para mal passada
59°C - Ao ponto
64°C - Ao ponto para bem passada
72°C - Bem passada
'''

tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Favor deixe cozinhar um pouco mais')
elif tem_cel in range(48, 53):
    print('Selada')
elif tem_cel in range(54, 59):
    print('Ao ponto para mal passada')
elif tem_cel in range(60, 64):
    print('Ao ponto')
elif tem_cel in range(65, 71):
    print('Ao ponto para bem passada')
elif tem_cel < 72:
    print('Bem passada')
else: 
    print('Carne queimou')
