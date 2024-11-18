print("Artikel: %5d, Preis: %8.2f" % (453, 59.058))

print('Fließkommazahl im Exponentialformat (in Kleinbuchstaben):')
print("%10.3e"% (356.08977))

print('Fließkommazahl im Exponentialformat (in Großbuchstaben).')
print("%10.3E"% (356.08977))

print('vorzeichenlose Ganzzahlen (oktal')
print("%10o"% (25))
print("%10.3o"% (25))#3 zeichen 031
print("%10.5o"% (25))# 5 00031

print('vorzeichenlose Ganzzahlen (hexadezimal')
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))

print("Ein Prozentzeichen: %% " % ())

print('# Wird dieses Zeichen mit o, x oder X benutzt, wird der jeweilige Wert mit dem entsprechenden folgenden Präfix: 0, 0o, 0O, 0x oder 0X')
print("%#5X"% (47))

print("%5X"% (47))

print("%#5.4X"% (47))#4 simbole, # steht für OX -hexadezimale Zahl

print("%#5o"% (25))

print("%+d"% (42))# + und ganzezahl 42

print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))


s = "Preis: $ %6.2f"% (356.08977)#6 zeichen, float, 2 simbolen nachdem komma
print(s)