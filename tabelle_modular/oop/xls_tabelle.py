from tabelle import Tabelle

class Xls_tabelle(Tabelle):

    #def ausgeben(self):
        pass

ascii_tabelle = erzeuge_ascii_tabelle()
tabelle = Xls_tabelle(ascii_tabelle)
tabelle.ausgeben()
