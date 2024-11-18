
class Tabelle:
    #tabellen_dict = dict()
    def __init__(self, tb_d):#hier ist es ein parametr
        self.tabellen_dict = tb_d  #hier ist es ein Atributt

    def ausgeben(self):
        self.kopf_ausgeben()
        n_zeilen = self.anzahl_zeilen()
        n_spalten = len(self.tabellen_dict.items())
        for zi in range(1, n_zeilen+1):
            dz = self.daten_zeile(zi)
            self.zeile_ausgeben(dz, zi)
        print("   "+("+---" * n_spalten) + "+")


#testen:
#t = Tabelle()
#print(type(t))


    def kopf_ausgeben(self):
        dz = []
        for sp_name in self.tabellen_dict.keys():
            dz.append(sp_name)
        self.zeile_ausgeben(dz, None)


    def anzahl_zeilen(self):
        # alle Spalten gleich lang
        sp_vs = self.tabellen_dict.values()
        for sp_d in sp_vs:
            return len(sp_d)
        
    def daten_zeile(self, zeilen_nr):
        dz = []
        for sp_i, sp_d in self.tabellen_dict.items():
            zi = 1
            for k, v in sp_d.items():
                if zi == zeilen_nr:
                # dz.append(k)
                    dz.append(v)
                zi += 1
        return dz
    
    def zeile_ausgeben(self, dz, zeilen_nr):
        if zeilen_nr:
            print(("   "+"+---" * len(dz)) + "+")
            print(f'{zeilen_nr:>3}', end="")
        else:
            print(f'   ', end="")
        for d in dz:
            p = f"{d:>3}"
            if isinstance(d, str):
                p = "   "
                if len(d) == 1:
                    d = bytes([ord(d)]).decode("cp437")
                    if d.isprintable():
                        p = f"{d:^3}"
                else:
                    p = f"{d:>3}"
            if zeilen_nr:
                print("|"+f"{p}", end="")
            else:
                print(" "+f"{p}", end="") 
        print("|"*int(bool(zeilen_nr)))


def erzeuge_ascii_tabelle():
    s = 0
    spalte = None
    ascii_t = dict()
    for i in range(32, 256):
        if (i - 32) % 32 == 0:
            s += 1
            spalte = dict()
            ascii_t[s] = spalte
        spalte[i] = chr(i)
    return ascii_t


ascii_tabelle = erzeuge_ascii_tabelle()
tabelle = Tabelle(ascii_tabelle)

ascii_tabelle2 = erzeuge_ascii_tabelle()
tabelle2= Tabelle(ascii_tabelle2 )

tabelle.ausgeben()

print(id(tabelle))
print(id(tabelle2))#sie sind unterschiedlich