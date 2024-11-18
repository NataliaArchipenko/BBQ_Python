import tabelle
#xls_tabelle
def erstell_exel_table(m_spalten, n_zeilen):
    exl_tab = dict()
    for sp in range(1, m_spalten+1):
        spalten_name = chr(ord('A') + (sp-1))
        spalte = erstelle_spalte(spalten_name, n_zeilen)
        #ex_tabelle_füge_spalte_hinzu(exl_tab, spalten_name, spalte)  
        exl_tab.update({spalten_name: spalte}) 
    return exl_tab

def erstelle_spalte(spalten_name, n_zeilen):
    spalte = dict()
    for z in range(1, n_zeilen + 1):
        zelle = erstelle_zellen_inhalt(spalten_name, z)
        spalte[z] = zelle
    return spalte

def erstelle_zellen_inhalt(spalten_name, zeilen_nr):
    return spalten_name + str(zeilen_nr)

#zelle_inhalt = erstelle_zelle_inhalt('A', 1)
#print(zelle_inhalt) 

#def ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte):
    #exl_tab.update(spalten_name, spalte)

super_tabelle = erstell_exel_table(10,11)
print(super_tabelle )
tabelle.tabelle_ausgeben(super_tabelle)

for spalten_name, spalte in super_tabelle.items():
    print(f"{spalten_name}: {spalte}")


def tabellen_zeile_ausgeben(dz):
    for d in dz:
        p = f"{d:>3}"
    if isinstance(d, str):
        p = "   "
        if len(d)==1:
            d = bytes([ord(d)]).decode("cp437")
            if d.isprintable():
                p = f"{d:>3}"
        else:
            p = f"{d:>3}"
        print(f"| {p}", end = "")
    print("|")

tabelle.tabelle_ausgeben(super_tabelle)