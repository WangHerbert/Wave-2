import random

response = input('Would you like to spin the roulette wheel? (y or n): ')

if response == 'y':
    spin = random.randint (1, 38)
else:
    print("That's too bad")
    quit ()

if spin == 37 or 38:
    if spin == 37:
        print ('The spin resulted in 0...')
        print ('Pay 0')
        quit ()
    elif spin == 38:
        print ('The spin resulted in 00...')
        print ('Pay 00')
        quit ()

print ("The spin resulted in %d..." % spin)

print ('Pay %d' % spin)

if spin % 2 != 0 and spin < 10 or spin % 2 == 0 and spin > 10 and spin < 19 \
    or spin % 2 != 0 and spin > 18 and spin < 28 or spin % 2 == 0 and spin > 29:
    print ('Pay Red')
else:
    print ('Pay Black')

if spin % 2 == 2:
    print ('Pay Even')
else:
    print ('Pay Odd')

if spin < 19:
    print ('Pay 1 to 18')
else:
    print ('Pay 19 to 36')