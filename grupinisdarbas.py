# Komandinis darbas - biudžeto programėlė
# Klasės
# Irasas (abstraktus) +

# savybė suma +
# savybė komentaras +
# Islaidos(Irasas) +

# savybė gavejas +
# Pajamos(Irasas) +

# savybė siuntejas +
# Biudzetas

# savybe zurnalas: sąrašas įrašų
# Biudzetas turi turėti metodus:

# ataskaitai
# balansas
# pajamų įrašo sukūrimas ir įtraukimui į žurnalą
# išlaidų įrašo sukūrimas ir įtraukimui į žurnalą
# Programos meniu ir funkcionalumą galite įgyvendinti tiek per klasę, tiek pagrindinėje programoje.
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()

class Irasas():
    def __init__(self, suma, komentaras):
        self.suma = suma
        self.komentaras = komentaras


class Islaidos(Irasas):
    def __init__(self, gavejas, suma, komentaras):
        super().__init__(suma, komentaras)
        self.gavejas = gavejas


class Pajamos(Irasas):
    def __init__(self, siuntejas, suma, komentaras):
        super().__init__(suma, komentaras)
        self.siuntejas = siuntejas


class Biudzetas():
    def __init__(self):
        self.zurnalas = []
    
    def pajamu_irasas(self,pajamos):
        self.zurnalas.append(pajamos)

    def islaidu_irasas(self,islaidos):
        self.zurnalas.append(islaidos)

    def itraukti_irasa(self, irasas):
        self.zurnalas.append(irasas)

biudzetas = Biudzetas()
pajamos = Pajamos(500, 'pajamos', siuntejas='Tadas')
biudzetas.pajamu_irasas(pajamos)
islaidos = Islaidos(300, 'islaidos', gavejas='Jonas')
biudzetas.islaidu_irasas(islaidos)

for vartotojas in biudzetas.zurnalas:
    if isinstance(vartotojas, Pajamos):
        print(f'{vartotojas.siuntejas} pajamos yra: {vartotojas.suma}')
    elif isinstance(vartotojas, Islaidos):
        print(f'{vartotojas.gavejas}, islaidos yra: {vartotojas.suma}')
    else:
        print("Nėra jokių įrašų apie tokį vartotoją.")

while True:
    print(' 1 - Peržiūrėti ataskaitą.\n '   
    '2 - Patikrinti esamą balansą. \n '
    '3 - Sukurti pajamų įrašą. \n '
    '4 - Sukurti išlaidų įrašą. \n '
    '0 - Išeiti iš meniu. \n ')
    pasirinkimas = int(input('Pasirinkite ką norite atlikti: '))
    

    if pasirinkimas == 1:
        clear()
        biudzetas.itraukti_irasa(Pajamos(siuntejas='tadas', suma=200, komentaras='test'))
        print(Pajamos)
    elif pasirinkimas == 2:
        clear()
        print("2 pasirinkimas")
    elif pasirinkimas == 3:
        clear()
        print("3 pasirinkimas")
    elif pasirinkimas == 4:
        clear()
        print("4 pasirinkimas")
    elif pasirinkimas == 0:
        clear()
        break
    else:
        clear()
        print('Tokio pasirinkimo nėra, prašome bandyti dar kartą.')
        