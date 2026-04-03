#  programa para adivinhar as musicas da lana del rey

print('🍒❤️‍🔥 LANA ❤️‍🔥🍒')

pontos = 0

musicas = [
    ('I hear the birds on the summer breeze, I drive fast \nI am alone at midnight', 'ride'),
    ('It isn\'t that hard, boy, to like you or love you? \nI\'d follow you down, down, down \nYou\'re unbelievable"?', 'million dollar man'),
    ('He used to call me poison \nLike I was poison ivy', 'ultraviolence'),
    ('Summer\'s meant for lovin\' and leavin\' \nI was such a fool for believin\' that you \nCould change all the ways you\'ve been livin\' \nBut you just couldn\'t stop', 'white mustang')
]

for frase, resposta_correta in musicas:
    song =''

    while song.lower() != resposta_correta:
        song = input(f'Qual música da Lana contém essa frase?\n"{frase}"\n')

        if song.lower() != resposta_correta:
            print('você errou :( tente novamente para passar para a próxima fase 🥺)')
            print(pontos)
        else:
            print('diva! você acertou! mais um ponto para você🌹')
            pontos += 1
            print(pontos)