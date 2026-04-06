bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

porcentagens = []

for bacteria in range(len(bacterias) - 1):
    bacteriaAtual = bacterias[bacteria]
    bacteriaSeguinte = bacterias[bacteria + 1]

    porcentagem = round((bacteriaSeguinte - bacteriaAtual) / (bacteriaAtual) * 100, 2)
    porcentagens.append(f'{porcentagem} %')




print(f'A porcentagem de crescimento em cada dia foi: {porcentagens}')