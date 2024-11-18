j = int(input('Jahr:'))
'''if j%4==0 and j%100==0 and j%400== 0 or j%4==0 and j%100!=0:
    print(f'{j} ist ein Schaltjahr')
else:
    print((f'{j} ist kein Schaltjahr'))'''

#Variante 2:
if j % 4 == 0:
    if j % 100 == 0:
        if j % 400 == 0:
            print(f'{j} ist ein Schaltjahr')
        else:
            print(f'{j} ist kein Schaltjahr')
    else:
        print(f'{j} ist ein Schaltjahr')
else:
    print(f'{j} ist kein Schaltjahr')


