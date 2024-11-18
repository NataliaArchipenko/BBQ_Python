# Funktion zum Erstellen der ASCII-Tabelle
def ascii_tabelle_erstellen():
    # Anzahl der Spalten
    spalten = 7
    
    # Bereich von ASCII-Zeichen
    start = 32
    ende = 256

    # Schrittweite, um die Tabelle zu füllen (jede Reihe hat 7 Werte)
    for i in range(start, ende, spalten):
        zeile = []
        for j in range(spalten):
            if i + j < ende:
                ascii_code = i + j
                zeile.append(f"{ascii_code:>3} | {chr(ascii_code):<3}")
            else:
                zeile.append("    ")  # Leere Werte, wenn die Spalten zu Ende sind
        # Ausgabe der Zeile
        print(" | ".join(zeile))

# Aufruf der Funktion
ascii_tabelle_erstellen()