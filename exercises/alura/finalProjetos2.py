par = []
impar = []
i = 0

while i < 10:
    ids = int(input('Digite o ID do produto: '))
    if ids % 2 == 0:
        par.append(ids)
    else:
        impar.append(ids)
    i +=1

print(f'A quantidade de doces é {len(par)} e de amargos é {(len(impar))}')