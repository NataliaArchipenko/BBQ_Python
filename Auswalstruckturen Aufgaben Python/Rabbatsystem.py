def rabbatberechnung(b):
    ermaessifung = [10, 15, 20]
    if b < 0:
        print('Ungültiger Wert. Geben Sie einencBestellwert größer als 0')
    elif 0 < b < 100:
        r = b * ermaessifung[0] / 100 # berechnen Rabbat (r) 10%
        b = b - r
        print(f' Ihre Rabbat erhaltet {ermaessifung[0]} %. Es ist {r} Euro. Der ermäßigte Bestellwert ist {b} Euro')
    elif 100 <= b < 500:
        r = b * ermaessifung[1] / 100 #berechnen Rabatt (r) 15 %
        b = b - r
        print(f' Ihre Rabbat erhaltet {ermaessifung[1]} %. Es ist {r} Euro. Der ermäßigte Bestellwert ist {b} Euro')
    else:
        r = b * ermaessifung[1] / 100 #berechnen Rabatt (r) 20 %
        b = b - r
        print(f' Ihre Rabbat erhaltet {ermaessifung[2]} %. Es ist {r} Euro. Der ermäßigte Bestellwert ist {b} Euro')

while True:
        bestellwert = float(input('Geben Sie einen Bestellwert ein: '))
        if bestellwert <= 0:
            print('Ungültiger Wert. Bitte geben Sie einen Bestellwert größer als 0 ein.')
        else:
            rabbatberechnung(bestellwert)  # Rabattberechnung aufrufen
            break  # Beendet die Schleife, wenn der Wert gültig ist
