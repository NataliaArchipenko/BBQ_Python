import os
s_feld = [
    [0, 0, 1, 0, 0, 2, 0, 0, 3],   #0 
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   #1
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   #2
    [0, 0, 4, 0, 0, 5, 0, 0, 6],   #3
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   #4 
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   #5 
    [0, 0, 7, 0, 0, 8, 0, 0, 9],   #6
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   #7
    [0, 0, 0, 0, 0, 0, 0, 0, 0] #8
]
def spiel_feld_anzeigen(feld):
    blau = '\033[34m'
    red = '\033[91m'
    fett = '\033[1m'
    green = '\033[92m'

    print(f' {' '*10}{fett}{red} SUDOKU')
    print(f'{green}+---------+---------+---------+')
    print(f'| {"  ".join(map(str, s_feld[0][0:3]))} | {"  ".join(map(str,s_feld[0][3:6]))} | {"  ".join(map(str,s_feld[0][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[1][0:3]))} | {"  ".join(map(str,s_feld[1][3:6]))} | {"  ".join(map(str,s_feld[1][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[2][0:3]))} | {"  ".join(map(str,s_feld[2][3:6]))} | {"  ".join(map(str,s_feld[2][6:]))} |')
    print('+---------+---------+---------+')
    print(f'| {"  ".join(map(str, s_feld[3][0:3]))} | {"  ".join(map(str,s_feld[3][3:6]))} | {"  ".join(map(str,s_feld[3][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[4][0:3]))} | {"  ".join(map(str,s_feld[4][3:6]))} | {"  ".join(map(str,s_feld[4][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[5][0:3]))} | {"  ".join(map(str,s_feld[5][3:6]))} | {"  ".join(map(str,s_feld[5][6:]))} |')
    print('+---------+---------+---------+')
    print(f'| {"  ".join(map(str, s_feld[6][0:3]))} | {"  ".join(map(str,s_feld[6][3:6]))} | {"  ".join(map(str,s_feld[6][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[7][0:3]))} | {"  ".join(map(str,s_feld[7][3:6]))} | {"  ".join(map(str,s_feld[7][6:]))} |')
    print(f'| {"  ".join(map(str, s_feld[8][0:3]))} | {"  ".join(map(str,s_feld[8][3:6]))} | {"  ".join(map(str,s_feld[8][6:]))} |')
    print('+---------+---------+---------+')

spiel_feld_anzeigen(s_feld)

# die Zahlen von 1 bis 9
a = int(input('Geben Sie eine Zahl von 1 bis 9 ein:'))
#Jede Zahl von 1 bis 9 darf in jeder Zeile nur einmal vorkommen
'''
for zeile in s_feld:
    gesehende_zahlen = set()
    for zahl in zeile:
        if zahl != 0:
            if zahl in gesehende_zahlen:
                print(f'Die Zahl {zahl} ist schon existiert, wählen Sie eine andere Zahl')
        else:
            gesehende_zahlen.add(zahl)
#Jede Zahl von 1 bis 9 in jeder Spalte darf nur einmal vorkommen
#eine spalte = s_feld[0][0] dann [1][0]

for spalte_index in range(len(s_feld[0])):
    gesehende_zahlen = set()
    for zahl in s_feld:
        zahl = zeile[spalte_index]
        if zahl !=0:
            if zahl in gesehende_zahlen:
                print(f'Die Zahl {zahl} ist schon existiert, wählen Sie eine andere Zahl')
            else:
                gesehende_zahlen.add(zahl)


 
#jede Zahl in jedem Quadrad kann nur ein mal vorkommen
ein Quadrad 
s_feld[0][0] s_feld[0][1] s_feld[0][2]
s_feld[1][0] s_feld[1][1] s_feld[1][2] 
s_feld[2][0] s_feld[2][1] s_feld[2][2] 

for spalte_index in range(len(s_feld[])):
    gesehende_zahlen = set()
    for zahl in spalte_index:
        if x != 0:'''




#Einige Felder sind zu Beginn des Spieles bereits ausgeführt. Man darf sie nicht verändern!

#Gewinn: Wenn alle Felder sind komplett ausgefühlt!
