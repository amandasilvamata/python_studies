number = int(input('Digite um número: '))

for produto in range(11):
    resultado = (number * produto)
    print(f'{number} X {produto} = {resultado}')