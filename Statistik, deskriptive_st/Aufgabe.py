def mittelwert(liste):
        return sum(liste)/len(liste)
    
liste= [1,8,4,5]
print(f' Mittelwert ist {mittelwert(liste)}')

def median(liste):
        sorted_liste = sorted(liste)
        print(sorted_liste)
        if len(sorted_liste) % 2 == 0: # gerade
                return (sorted_liste[len(sorted_liste)//2] +(sorted_liste[len(sorted_liste)//2] -1))/2
        else:
                return(sorted_liste[len(sorted_liste)//2])   
                
print(f' Midian ist {median(liste)}')

def modus(liste): #modus - wie oft treffen wir eine Wert in der Liste
        haeuftigkeit = {}
        for el in liste:
            if el in haeuftigkeit:
                    haeuftigkeit[el] += 1
            else:
                    haeuftigkeit[el] = 1
        max_haeftig = 0
        for key, value in  haeuftigkeit.items():
            if value > max_haeftig:
                    max_haeftig = value  
                    modus = key
        return modus     

print(f' Modus ist {modus(liste)}')   

def varianz(liste):
       #Varianz = (xi - mittelwert)^2 / n, wo xi = el, n = len(liste)
    sum_qw = 0
    for el in liste:
        sum_qw += (el - mittelwert(liste))**2

    return sum_qw / len(liste)  
print(f' Varianz ist {varianz(liste)}')

def standardabweichung(liste):
    pass
