number = int(input('Enter a number '))

for factors in range(11):
    product = (number * factors)
    print(f'{number} X {factors} = {product}')