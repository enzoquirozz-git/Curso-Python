primero = input('ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'
if primero == 'chanchito feliz':
    print ('el valor ingresado no es un numero')
    exit()

segundo = input('ingrese segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'
if segundo == 'chanchito feliz':
    print ('el valor ingresado no es un numero')
    exit()

if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('el valor ingresado no es un numero')
else:
    print (primero + segundo)
