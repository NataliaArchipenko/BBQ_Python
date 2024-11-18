#R = U/I
#Variante mit IF:
'''def wiederstand(U,I):
    return U/I
def leistung(R,I):
    return I*R
def strom(U,R):
    return U/R

a = input('Geben Sie R, U oder I ein:')
groesse = ['r', 'u', 'i']
a = a.lower()
if a not in groesse:
    print('Das ist ein falsches Zeichne, geben Sie R, U oder I ein')
else:
    if a == 'r':
        U = int(input('Geben Sie die Spannung (U) in Volt ein: '))
        I = int(input('Geben Sie die Stromstärke (I) in Ampere ein: '))
        print(f'Der Widerstand (R) ist {wiederstand(U, I)} Ohm')
    elif a == 'u':
        R = int(input('Geben Sie den Widerstand (R) in Ohm ein: '))
        I = int(input('Geben Sie die Stromstärke (I) in Ampere ein: '))
        print(f'Die Spannung ist {leistung(R,I)} Volt')
    elif a == 'i':
        R = int(input('Geben Sie den Widerstand (R) in Ohm ein: '))
        U = int(input('Geben Sie die Spannung (U) in Volt ein: '))
        print(f'Die Stromstärke ist {round(strom(U,R),2)} Ampere')'''

def widerstand(U, I):
    return U / I

def leistung(U, I):
    return U * I

def strom(U, R):
    return U / R

while True:
    a = input('Geben Sie R (Widerstand), U (Spannung) oder I (Strom) ein: ').lower()
    
    if a != 'r' and a != 'u' and a != 'i':
        print('Fehlermeldung: Geben Sie R, U oder I ein.')
        break  # Beenden das Programm bei falscher Eingabe

    try:
        if a == 'r': 
            U = float(input('Geben Sie die Spannung (U) in Volt ein: '))
            I = float(input('Geben Sie die Stromstärke (I) in Ampere ein: '))
            print(f'Der Widerstand beträgt {widerstand(U, I)} Ohm.')
        elif a == 'u': 
            R = float(input('Geben Sie den Widerstand (R) in Ohm ein: '))
            I = float(input('Geben Sie die Stromstärke (I) in Ampere ein: '))
            print(f'Die Spannung beträgt {leistung(R, I)} Volt.')
        elif a == 'i':  
            U = float(input('Geben Sie die Spannung (U) in Volt ein: '))
            R = float(input('Geben Sie den Widerstand (R) in Ohm ein: '))
            print(f'Die Stromstärke beträgt {strom(U, R)} Ampere.')
    except ValueError:
        print('Fehler: Bitte geben Sie gültige Zahlen ein.')