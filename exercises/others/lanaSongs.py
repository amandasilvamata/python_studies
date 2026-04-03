#  programa para adivinhar as musicas da lana del rey

print('************LANA *******************')

song = ""
pontos = 0

while song != 'ride' and song != 'Ride':
    song = input('Qual música da Lana contém essa frase? \n"I hear the birds on the summer breeze, I drive fast \n I am alone at midnight"? ')
    if song != 'ride' and song != 'Ride':
        print('você errou :( tente novamente para passar para próxima fase)')
        print(pontos)
    else:
        print('Diva! você acertou! Mais um ponto!')
        pontos += 1
        print(pontos)

while song != 'million dollar man' and song != 'Million Dollar Man':
    song = input('Qual música da Lana contém essa frase?\n"It isn\'t that hard, boy, to like you or love you? \nI\'d follow you down, down, down \nYou\'re unbelievable"? ')
    if song != 'million dollar man' and song != 'Million Dollar Man':
        print('você errou :( tente novamente para passar para próxima fase)')
        print(pontos)
    else:
        print('Diva! você acertou! Mais um ponto!')
        pontos += 1
        print(pontos)

