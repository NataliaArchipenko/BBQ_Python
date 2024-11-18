'''def calculate(a, op,b):
    operation = get_implementation_of_operation(op)
    result = operation(a,b)
    return result

def get_implementation_of_operation(op):
    dic = {'+': addition, '-': substraktion, '*': multiplikation, '/': division}
    return dic[op] # {'+': addition, '-': substraktion, '*': multiplikation, '/': division}.get(op)
    #return {'+': addition, '-': substraktion, '*': multiplikation, '/': division}.get(op)
    #return {'+': addition, '-': substraktion, '*': multiplikation, '/': division}[op]
    if op == '+':
        return addition
    elif op == '-':
        return substraktion
    elif op == '*':
        return multiplikation
    elif op == '/':
        return division
    
def addition(a,b):
    return a + b
def substraktion(a,b):
    return a - b
def multiplikation(a,b):
    return a * b
def division(a,b):
    if b !=0:
        return a/b
    else:
        return 'Fehlermeldung: Man darf auf Null nicht teilen'

print(calculate(11, '+', 5))
print(calculate(11, '-', 5))  
print(calculate(11, '*', 5))  
print(calculate(11, '/', 5))  



von Julia:
def get_implementation_of_operation(op):
    return {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }.get(op, None)'''

# erstellen Sie zufällig 20 Argument-Sätze und lassen jeweil einen Wert berechnen 
# und fügen diesen Wert in eine Liste ein.

import random # Importieren der Funktion "random"
def calculate(a, op,b):
    operation = get_implementation_of_operation(op)
    result = operation(a,b)
    return result

def get_implementation_of_operation(op):
    return {'+': addition, '-': substraktion, '*': multiplikation, '/': division}[op]

def addition(a,b):
    return a + b
def substraktion(a,b):
    return a - b
def multiplikation(a,b):
    return a * b
def division(a,b):
    if b !=0:
        #return round(a/b,2)# 2 Zeichen nach dem Komma mit der Funktion round
        return (f'{a/b:.2f}') # 2 Zeichen nach dem Komma
    else:
        return 'Fehlermeldung: Man darf auf Null nicht teilen'
    
liste_mit_loesungen= [] # leer liste für die Lösungen

for _ in range(20):# 20 Variante
    a = random.randint(1, 100)  # Erste Zufallszahl, die  von 1 bis 100 ausgewählt wurde
    b = random.randint(1, 100)  # Zweite Zufallszahl, die  von 1 bis 100 ausgewählt wurde
    op = random.choice(['+', '-', '*', '/']) # nimmt operator zufählig  
    result = calculate(a, op, b)  # Berechnung
    print (f' {a} {op} {b} = {result}')#Man kann jedes Ergebniss anschauen
    liste_mit_loesungen.append(result)# Lösungen in der Liste hinzufügen  
print(liste_mit_loesungen)



import random

c_l = [((a,op,b), calculate(a, op, b)) for (a,op,b) in 
       [(random.randint(1,100), random.choice(['+', '-', '*', '/']), random.randint(1,100)) for i in range(20)]]
for c_e in c_l:
    print(f"()")