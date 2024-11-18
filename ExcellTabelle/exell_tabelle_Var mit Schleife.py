excell = {
'A' :{1:'A1',2:'A2',3:'A3',4:'A4',5:'A5',6:'A6',7:'A7',8:'A8',9:'A9',10:'A10',11:'A11'},
'B' :{1:'B1',2:'B2',3:'B3',4:'B4',5:'B5',6:'B6',7:'B7',8:'B8',9:'B9',10:'B10',11:'B11'},
'C' :{1:'C1',2:'C2',3:'C3',4:'C4',5:'C5',6:'C6',7:'C7',8:'C8',9:'C9',10:'C10',11:'C11'},
'D' :{1:'D1',2:'D2',3:'D3',4:'D4',5:'D5',6:'D6',7:'D7',8:'D8',9:'D9',10:'D10',11:'D11'},
'E' :{1:'E1',2:'E2',3:'E3',4:'E4',5:'E5',6:'E6',7:'E7',8:'E8',9:'E9',10:'E10',11:'E11'},
'F' :{1:'F1',2:'F2',3:'F3',4:'F4',5:'F5',6:'F6',7:'F7',8:'F8',9:'F9',10:'F10',11:'F11'},
'G' :{1:'G1',2:'G2',3:'G3',4:'G4',5:'G5',6:'G6',7:'G7',8:'G8',9:'G9',10:'G10',11:'G11'},
'H' :{1:'H1',2:'H2',3:'H3',4:'H4',5:'H5',6:'H6',7:'H7',8:'H8',9:'H9',10:'H10',11:'H11'},
'I' :{1:'I1',2:'I2',3:'I3',4:'I4',5:'I5',6:'I6',7:'I7',8:'I8',9:'I9',10:'I10',11:'I11'},
'J' :{1:'J1',2:'J2',3:'J3',4:'J4',5:'J5',6:'J6',7:'J7',8:'J8',9:'J9',10:'J10',11:'J11'},
'K' :{1:'K1',2:'K2',3:'K3',4:'K4',5:'K5',6:'K6',7:'K7',8:'K8',9:'K9',10:'K10',11:'K11'}}
#in die Tabelle andere Werte hinzufügen
wert = 'Hallo'
excell['A'][4] = wert
excell['B'][8] = 'Nata'

#Erstellen der Kopfzeile 
column_namen = ['A','B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for i in range(12):
    print('+--------', end = '')
print('+')

print(f'|{" ":^7}', end=" ")

for column in column_namen:
    print(f'|{column:^7}', end=" ")   
print('|')

for i in range(12):
    print('+--------', end = '')
print('+')

#Erstellen erste Spalte mit nummer und Inhalt
for num in range(1,12):
    print(f'| {num:^6}', end = '') 

    for column in column_namen:
        print(f' | {excell[column][num]:^6}', end= '')    
    print(' |')
# trennen Zeilen 
    for i in range(12):
        print('+--------', end = '')
    print('+')
