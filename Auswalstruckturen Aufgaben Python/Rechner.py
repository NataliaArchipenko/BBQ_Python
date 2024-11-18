#Rechner

def rechner(Zahl1, Zahl2, Zeichen):
    a = Zahl1
    b = Zahl2
    
    if Zeichen == '+':
        return a + b
    elif Zeichen == '-':
        return a - b
    elif Zeichen == '*':
        return a * b
    elif Zeichen == '/':
        return a / b
    else:
        return 'Fehlermeldung'
    
print(rechner(3, 2, '+'))

# Funktionloeser
def funktionloeser(Zahl):
    x = Zahl
    e = 2.718
    if x <= 0:
        return e**x # expontionel
    elif 0 < x <=3:
        return x**2 + 1 #quadratisch
    elif x > 3:
        return 2 * x + 4 # linear
    else:
        return 'Fehlemeldung'

print(f'Ergebnis ist {funktionloeser(3)}')
print(f'Ergebnis ist {funktionloeser(-3)}')
print(f'Ergebnis ist {funktionloeser(2)}')

#R = U/I
a = input('Geben Sie R, U oder I ein:')
groesse = ['r', 'u', 'i']
a = a.lower()
if a not in groesse:
    print('Falsch')
else:
    print('richtig')




