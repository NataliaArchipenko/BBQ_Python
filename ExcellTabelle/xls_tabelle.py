import tabelle

def erstelle_excel_tabelle(m_spalten, n_zeilen):
    ex_tab = dict()
    for sp in range(1, m_spalten+1):
        spalten_name = chr(ord('A')+(sp-1))
        spalte = erstelle_spalte(spalten_name, n_zeilen)
        # ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte)
        ex_tab.update({spalten_name: spalte})
    return ex_tab

def erstelle_spalte(spalten_name, n_zeilen):
    spalte = dict()
    for z in range(1,n_zeilen+1):
        zelle = erstelle_zellen_inhalt(spalten_name, z)
        spalte[z] = zelle

    return spalte


def erstelle_zellen_inhalt(spalten_name, zeilen_nr):
    return spalten_name+str(zeilen_nr)


def ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte):
    ex_tab.update(spalten_name, spalte)


super_tabelle = erstelle_excel_tabelle(11, 10)

print(super_tabelle)

tabelle.tabelle_ausgeben(super_tabelle)