import tabelle

excel_tabelle = {
    "A": {
        1: "A1",
        2: "A2",  # und so weiter
        # ...
        11: "A11",
    },
    "B": {
        1: "B1",
        2: "B2",  # und so weiter
        # ...
        11: "B11",
    },
    # und so weiter
}


def erstelle_excel_tabelle(m_spalten, n_zeilen):
    ex_tab = dict()
    for sp in range(1, m_spalten + 1):
        spalten_name = chr(ord("A") + (sp - 1))
        spalte = erstelle_spalte(spalten_name, n_zeilen)
        # ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte)
        ex_tab.update({spalten_name: spalte})
    return ex_tab


def erstelle_spalte(spalten_name, n_zeilen):
    spalte = dict()
    for z in range(1, n_zeilen + 1):
        zelle = erstelle_zellen_inhalt(spalten_name, z)
        spalte[z] = zelle

    return spalte


def erstelle_zellen_inhalt(spalten_name, zeilen_nr):
    return spalten_name + str(zeilen_nr)


def ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte):
    ex_tab.update({spalten_name: spalte})


def ex_tabelle_zellenwert(ex_tab, spalte, zeile):  # ('B', 2)
    return ex_tab[spalte][zeile]


def ex_tabelle_setze_zellenwert(ex_tab, spalte, zeile, neuer_wert):
    alter_wert = ex_tabelle_zellenwert(ex_tab, spalte, zeile)
    ex_tab[spalte][zeile] = neuer_wert
    return alter_wert


# A2=17
def ex_tabelle_setze_wertformel(ex_tabelle, wert_formel):
    zs = wert_formel.split("=")  # => ['A2', '17']
    adr = zs[0]
    wert = zs[1]
    spalte = adr[0]
    zeile = int(adr[1:])
    return ex_tabelle_setze_zellenwert(ex_tabelle, spalte, zeile, wert)


def ex_tabelle_zu_CSV(ex_tabelle):
    spaltennamen = ex_tabelle.keys()
    csv = ""
    for sp in spaltennamen:
        csv += f",{sp}"
    csv += "\n"
    n_zeilen = tabelle.anzahl_zeilen(ex_tabelle)

    for z in range(1, n_zeilen + 1):
        csv += str(z)
        for sp in spaltennamen:
            wert = ex_tabelle_zellenwert(ex_tabelle, sp, z)
            csv += f",{wert}"
        csv += "\n"

    #
    #  ex_tabelle zu einem CSV-String

    return csv


def ex_tabelle_speichern_als_CSV(ex_tabelle, dateiname):
    csv = ex_tabelle_zu_CSV(ex_tabelle)
    # in Datei speichern
    with open(dateiname, "w") as datei:
        datei.write(csv)


def ex_tabelle_erstelle_kopfzeile(ex_tabelle, zeile_str):
    kopfzeile = zeile_str.split(",")
    for i in range(1, len(kopfzeile)):
        spaltenname = kopfzeile[i].strip()
        ex_tabelle_füge_spalte_hinzu(ex_tabelle, spaltenname, dict())


def ex_tabelle_erstelle_datenzeile(ex_tabelle, zeile_str):
    zeilennummer = 0
    daten = zeile_str.split(",")
    if len(daten):
        zeilennummer = int(daten[0].strip())
        spalten_index = 1
        for spalten_dict in ex_tabelle.values():
            spalten_dict.update({zeilennummer: daten[spalten_index].strip()})
            spalten_index += 1


def ex_tabelle_von_CSV_laden(dateiname):
    ex_tabelle = None
    with open(dateiname, "r") as datei:
        ex_tabelle = dict()
        zeile_str = datei.readline()
        ex_tabelle_erstelle_kopfzeile(ex_tabelle, zeile_str)
        zeile_str = datei.readline()
        while zeile_str:
            ex_tabelle_erstelle_datenzeile(ex_tabelle, zeile_str)
            zeile_str = datei.readline()
    return ex_tabelle


if __name__ == "__main__":
    # super_tabelle = erstelle_excel_tabelle(11, 10)
    super_tabelle = ex_tabelle_von_CSV_laden("super_tabelle.csv")
    tabelle.tabelle_ausgeben(super_tabelle)
    formel = input("Geben Sie die Formel an: ")
    alter_zellenwert = ex_tabelle_setze_wertformel(super_tabelle, formel)
    tabelle.tabelle_ausgeben(super_tabelle)
    print("alter Zellenwert:", alter_zellenwert)

    print(ex_tabelle_zu_CSV(super_tabelle))

    ex_tabelle_speichern_als_CSV(super_tabelle, "super_tabelle.csv")
