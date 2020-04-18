column = (input('Enter the column of the square: '))
row = int(input('Enter the row of the square: '))

if ord(column) % 2 == 0:
    if row % 2 == 0:
        print (column + str(row) + ' is a black square')
    else:
        print (column + str(row) + ' is a white square')

elif ord(column) != 0:
    if row % 2 == 0:
        print (column + str(row) + ' is a white square')
    else:
        print (column + str(row) + ' is a black square')