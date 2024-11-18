import tabelle
def erstelle_excel_tabelle(m_spalten, n_zeilen):
    ex_tab = dict() #das wird eine dictionary
    for sp in range(1, m_spalten+1):#fangen von 1 an, deswegen (sp-1) = um 0 zu erhalten
        spalten_name = chr(ord('A') + (sp - 1))#Die Funktion ord() gibt die Zahl zurück, die den Unicode-Code eines bestimmten Zeichens darstellt.
        spalte = erstelle_spalte(spalten_name, n_zeilen)#diese Funktion muss man  definieren
        ex_tab.update({spalten_name: spalte})# fügt die spalte_name als key und spalte als wert in dictionary hinzu
    return ex_tab
    
def erstelle_spalte(spalten_name, n_zeilen):
    spalte = dict()# Erstellen dictionary für die Spalte
    for z in range(1,n_zeilen+1):#von 1 bis zum n_zeilen inklusive(deswegen +1)
        zelle = erstelle_zellen_inhalt(spalten_name, z)#zelle ist ячейка, z = num z.b von 1 bis 11, hier gehr es um inhalt der Zelle
        spalte[z] = zelle
    return spalte

def erstelle_zellen_inhalt(spalten_name, zeilen_nr):
    return spalten_name + str(zeilen_nr) # z.b A + 1 als string das ist Inhalt der Zelle

# das haben wir schon oben geschrieben(es ist wie zweiter Variante)
def ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte):
    ex_tab[spalten_name] = spalte # fügt die spalte_name als key und spalte als wert in dictionary hinzu

#Funktion print muss man weiter bearbeiten
def print_tabelle(ex_tab):
    # Header der Tabelle drucken
    header = [""] + list(ex_tab.keys())  # Header mit leerem Element für die Zeilennummer
    print(" | ".join(header))  # Drucken des Headers
    print("-" * (len(header) * 8 - 4))  # Unterstrich für die Trennung
    
    # Zeilen der Tabelle drucken
    for i in range(1, len(next(iter(ex_tab.values()))) + 1):  # Iteration über die Zeilen
        row = [str(i)] + [ex_tab[col][i] for col in ex_tab.keys()]  # Hinzufügen der Zeilennummer
        print(" | ".join(f"{item: <5}" for item in row))  # Drucken der Zeile mit Formatierung

super_tabelle = erstelle_excel_tabelle(11, 10)#Aufruf der Funktion
print(print_tabelle(super_tabelle))

#$A$2 = 17
#Tauschen den Wert von unserer Tabelle:
def ex_tabelle_setzte_wert(ex_tab, spalte, zeile, wert):
    ex_tab[spalte][zeile]=wert # im Dictionary ex_tab wird der Wert in der angegebenen Zelle, definiert durch Spalte und Zeile, gesetzt.

#Einen Wert in die Tabelle hinzufügen:
'''def ex_tabelle_setzte_wertformel(ex_tab, wert_formel):
    zs = wert_formel.split("=") # ['A2', '17']  Die Formel wird in zwei Teile aufgespalten ['A2', '17']
    adr = zs[0] #'A2' - Adresse der Zelle: index = 0
    wert = zs[1] # '17' ist den Wert: index = 1
    spalte = adr[0] # Der erste Teil der Zellenadresse ist die Spalte  'A'
    zeile = int(adr[1:]) #Das Rest( in A2 es ist 2 mit index=1)
    return ex_tabelle_setzte_wert(ex_tab, spalte, zeile, wert)

if __name__ == '__main__':  # Erstellem einer Tabelle mit 11 Spalten und 10 Zeilen
    super_tabelle = erstelle_excel_tabelle(11,10)
    tabelle.tabelle_ausgeben(super_tabelle) # Gibt die Tabelle aus (diese Funktion befindet sich in Datei 'tabelle.py')
    formel = input("Geben Sie die Formel an:") # Aingabe von Benutzer: z.B. "A2=17"
    alter_zellenwert = ex_tabelle_setzte_wertformel(super_tabelle, formel) # Zelle wurde bestinmmt und neuen Wert eingesetzt 
    print("alter Zellenwert:", alter_zellenwert)'''


import csv
import io

def ex_tabelle_zu_CSV(ex_tabelle):
    """
    Konvertiert die Tabelle (ex_tabelle) in einen CSV-String.
    """
    output = io.StringIO()  # Erstellt einen Speicher-Puffer, der als Datei fungiert, aber in den Speicher schreibt.
    writer = csv.writer(output, delimiter=';')  # Erstellt einen CSV-Schreiber, der in den Speicher-Puffer schreibt. Das Semikolon wird als Trennzeichen verwendet.
    
    # Header schreiben (Spaltennamen)
    header = list(ex_tabelle.keys())  # Liste der Spaltennamen aus den Dictionary-Schlüsseln
    writer.writerow(header)  # Schreiben der Kopfzeile
    
    # Bestimmen der Anzahl der Zeilen (basierend auf einer Spalte)
    zeilen_anzahl = len(next(iter(ex_tabelle.values())))  # Anzahl der Zeilen in der Tabelle
    
    # Schreiben der Datenzeilen
    for i in range(1, zeilen_anzahl + 1):
        # Erstellen der Zeile: Hole die Werte aus jeder Spalte der Tabelle für die Zeile `i`
        row = [ex_tabelle[spalte][i] for spalte in ex_tabelle.keys()]
        writer.writerow(row)  # Schreiben der Zeile
    
    csv_string = output.getvalue()  # Den CSV-String aus dem Puffer extrahieren
    output.close()  # Schließen des Puffers
    
    return csv_string  # Rückgabe des CSV-Strings

def ex_tabelle_speichern_als_csv(ex_tabelle, dateiname):
    """
    Speichert die Tabelle (ex_tabelle) in einer CSV-Datei.
    """
    csv_string = ex_tabelle_zu_CSV(ex_tabelle)  # Konvertiert die Tabelle in einen CSV-String
    
    # Öffnen der Datei zum Schreiben
    with open(dateiname, 'w') as file:
        file.write(csv_string)  # Schreibe den CSV-String in die Datei


def ex_tabelle_von_CSV_laden(dateiname):
    """
    Lädt eine Tabelle aus einer CSV-Datei und konvertiert sie in das ex_tabelle-Format (Dictionary).
    """
    ex_tabelle = {}  # Leeres Dictionary für die Tabelle
    
    # Öffnen der Datei zum Lesen
    with open(dateiname, 'r') as file:
        reader = csv.reader(file, delimiter=';')  # CSV-Reader mit Semikolon als Trennzeichen
        header = next(reader)  # Erste Zeile als Header (Spaltennamen)
        
        # Initialisiere das Dictionary mit leeren Spalten (leere Dicts)
        for spalten_name in header:
            ex_tabelle[spalten_name] = {}
        
        # Zeilenweise Daten lesen
        zeile_nr = 1
        for row in reader:
            # Jede Spalte der Zeile wird der entsprechenden Spalte in ex_tabelle hinzugefügt
            for idx, spalten_name in enumerate(header):
                ex_tabelle[spalten_name][zeile_nr] = row[idx]  # Setze den Wert in der Zelle
            zeile_nr += 1  # Erhöhe die Zeilennummer
    
    return ex_tabelle  # Rückgabe der geladenen Tabelle


# 1. Eine Tabelle als CSV-String erstellen
super_tabelle = erstelle_excel_tabelle(3, 5)
csv_string = ex_tabelle_zu_CSV(super_tabelle)
print(csv_string)

# 2. Die Tabelle als CSV-Datei speichern
ex_tabelle_speichern_als_csv(super_tabelle, "tabelle.csv")

# 3. Eine Tabelle aus einer CSV-Datei laden
geladene_tabelle = ex_tabelle_von_CSV_laden("tabelle.csv")
print(geladene_tabelle)


ex_tabelle_von_CSV_laden(books)