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
    zurnalas = []
    def asd(self):
        print(self.zurnalas)
    
    def itraukti_irasa(self, irasas):
        self.zurnalas.append(irasas)

    def ataskaita(self):
        for irasas in biudzetas.zurnalas:
            if isinstance(irasas, Pajamos):
                print(f'{irasas.siuntejas}: pajamos yra: {irasas.suma}')
            elif isinstance(irasas, Islaidos):
                print(f'{irasas.gavejas}: išlaidos yra: {irasas.suma}')
            else:
                print("Blogas įrašas")

    def balansas(self):
        visos_pajamos = 0
        visos_islaidos = 0
        for balansas in biudzetas.zurnalas:
            if isinstance(balansas, Pajamos):
                visos_pajamos += balansas.suma 
            elif isinstance(balansas, Islaidos):
                visos_islaidos += balansas.suma 
        print(f"Balansas: {visos_pajamos - visos_islaidos}")

biudzetas = Biudzetas()

while True:
    print(' 1 - Peržiūrėti ataskaitą.\n '   
    '2 - Patikrinti esamą balansą. \n '
    '3 - Sukurti pajamų įrašą. \n '
    '4 - Sukurti išlaidų įrašą. \n '
    '0 - Išeiti iš meniu. \n ')
    pasirinkimas = int(input('Pasirinkite ką norite atlikti: '))
    

    if pasirinkimas == 1:
        clear()
        biudzetas.ataskaita()
    elif pasirinkimas == 2:
        clear()
        biudzetas.balansas()
    elif pasirinkimas == 3:
        clear()
        pajamos = float(input("Įveskite savo pajamas: "))
        komentaras = input('Įveskite komentarą: ')
        siuntejas = input("Įveskite siuntėją: ")
        biudzetas.itraukti_irasa(Pajamos(siuntejas, pajamos, komentaras))
        clear()
        print('Sukurtas pajamų įrašas')
    elif pasirinkimas == 4:
        clear()
        islaidos = float(input("Iveskite savo išlaidos: "))
        komentaras = input('Įveskite komentarą: ')
        gavejas = input("Įveskite siuntėją: ")
        biudzetas.itraukti_irasa(Islaidos(gavejas, islaidos, komentaras))
        clear()
        print('Sukurtas išlaidų įrašas')
    elif pasirinkimas == 0:
        clear()
        break
    else:
        clear()
        print('Tokio pasirinkimo nėra, prašome bandyti dar kartą.')
        
