import math

a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))


if b**2 - 4*a*c < 0:
    print ('There are no real zeros')

elif b**2 - 4*a*c == 0:
    print ('There is one real zero')
    print (-b / 2*a + ' is the real zero')

else: 
    print ('There are two real zeros')
    descrim = math.sqrt(b**2 - 4*a*c)
    print (str((-b + descrim)/ (2*a)) + ' and ' + str(((-b) - descrim)/ (2*a)) + ' are the two real zeros')