# BMI Version 1
'''a = float(input('Geben Sie Ihre Körpergewicht in kg ein'))
b = float(input('Geben Sie Ihre Körpergroße in sm ein'))
g = input('Geben Sie Ihre Geschlecht  m oder w ein').lower()
BMI = a / (b/100)**2
if BMI > 40:
    print(f'Ihre BMI ist {BMI} massive Adipositas')
elif 30 < BMI <= 40:
    print(f'Ihre BMI ist {BMI} Adipositas')
else:
    if g == 'w':
        if 24 < BMI <= 30:
            print(f'Ihre BMI ist {BMI} Übergewicht')
        elif 19 <= BMI <= 24:
            print(f'Ihre BMI ist {BMI} Normalgewicht')
        else:
            print(f'Ihre BMI ist {BMI} Untergewicht')
    elif g == 'm':
        if 25 < BMI <= 30:
            print(f'Ihre BMI ist {BMI} Übergewicht')
        elif 20 <= BMI <= 25:
            print(f'Ihre BMI ist {BMI} Normalgewicht')
        else: 
            print(f'Ihre BMI ist {BMI} Untergewicht')
    else:
        print('Ungültige Eingabe. Bitte geben Sie "m" für männlich oder "w" für weiblich ein.')'''

# BMI Version 2
def berechne_bmi(gewicht, groesse):
    return gewicht / (groesse / 100) ** 2

def klassifiziere_bmi(bmi, geschlecht):
    if bmi > 40:
        return 'massive Adipositas'
    elif 30 < bmi <= 40:
        return 'Adipositas'
    # w/m unterschied:
    if geschlecht == 'w':
        if 24 < bmi <= 30:
            return 'Übergewicht'
        elif 19 <= bmi <= 24:
            return 'Normalgewicht'
        else:
            return 'Untergewicht'
    elif geschlecht == 'm':
        if 25 < bmi <= 30:
            return 'Übergewicht'
        elif 20 <= bmi <= 25:
            return 'Normalgewicht'
        else:
            return 'Untergewicht'
    else:
        return 'Fehlermeldung: Ungültiges Geschlecht.'

gewicht = float(input('Geben Sie Ihr Körpergewicht in kg ein: '))
groesse = float(input('Geben Sie Ihre Körpergröße in cm ein: '))

while True:
    geschlecht = input('Geben Sie Ihr Geschlecht (m oder w) ein: ').lower()
    if geschlecht in ['m', 'w']:
        break
    else:
        print('Fehler: Ungültige Eingabe. Bitte geben Sie "m" für männlich oder "w" für weiblich ein.')

bmi = berechne_bmi(gewicht, groesse)

ergebnis = klassifiziere_bmi(bmi, geschlecht)
print(f'Ihr BMI beträgt {bmi:.2f}. {ergebnis}')
