"""
Hegycsúcs neve;Hegység;Magasság
Ágasvár;Mátra;789
Bálvány;Bükk-vidék;956
Büszkés-hegy;Bükk-vidék;952
Cserepes-kő;Bükk-vidék;823
"""

class Hegyek:
    def __init__(self,sor):
        hegycsucs,hegyseg,magassag = sor.strip().split(";")
        self.hegycsucs  = hegycsucs
        self.hegyseg    = hegyseg
        self.magassag   = int(magassag)


#1-2.feladat
with open("hegyekMo.txt",encoding="UTF-8")as f:
    fejlec = f.readline()
    lista = [Hegyek(sor) for sor in f]
#3.feladat
hegyek = [sor.hegycsucs for sor in lista]
print(f" 3. feladat: Hegycsúcsok száma: {len(hegyek)} db")
#4.feladat
atlag_magassag = [sor.magassag for sor in lista]
print(f" 4. feladat: Hegycsúcsok átlagos magassága: {sum(atlag_magassag) / len(atlag_magassag)} m") 
#5.feladat
print(f"5. feladat: A legmagasabb hegycsúcs adatai:")

legmagasabb = [(sor.magassag,sor) for sor in lista]
nagy,adat = max(legmagasabb)

print(f"""        Név: {adat.hegycsucs} 
        Hegység: {adat.hegyseg}
        Magasság: {nagy} m """)







