values = input().strip().split(' ')

if len(values) == 0:
    print('Error')
else:
    try:
        numbers = [int(i) for i in values]
        average = str(round(sum(numbers) / len(numbers), 2))
        if len(average.split('.')[1]) == 1:
            average += '0'
        print(average)
    except:
        print('Error: Asegurate de ingresar numeros validos.')
    