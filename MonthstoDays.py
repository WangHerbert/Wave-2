month = input('Enter a month (capitalize the first letter): ')

if month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print (month + ' has 30 days in it')

elif month == 'February':
    print (month + ' has 28 or 29 days in it')

else:
    print (month + ' has 31 days in it')