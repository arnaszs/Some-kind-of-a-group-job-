import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pajamu_menu():
    clear()
    pajamos = float(input("Įveskite savo pajamas: "))
    komentaras = input('Įveskite komentarą: ')
    siuntejas = input("Įveskite siuntėją: ")
    biudzetas.itraukti_irasa(Pajamos(siuntejas, pajamos, komentaras))
    clear()
    print('Sukurtas naujas pajamų įrašas. \n')
    
def islaidu_menu():
    clear()
    islaidos = float(input("Įveskite savo išlaidas: "))
    komentaras = input('Įveskite komentarą: ')
    gavejas = input("Įveskite siuntėją: ")
    biudzetas.itraukti_irasa(Islaidos(gavejas, islaidos, komentaras))
    clear()
    print('Sukurtas naujas išlaidų įrašas. \n')
    
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
    __zurnalas = []
    def asd(self):
        print(self.__zurnalas)
    
    def itraukti_irasa(self, irasas):
        self.__zurnalas.append(irasas)

    def ataskaita(self):
        clear()
        for irasas in biudzetas.__zurnalas:
            if isinstance(irasas, Pajamos):
                print(f'{irasas.siuntejas}: pajamos yra: {irasas.suma} € \n')
            elif isinstance(irasas, Islaidos):
                print(f'{irasas.gavejas}: išlaidos yra: {irasas.suma} € \n')
            else:
                print("Blogas įrašas \n")

    def balansas(self):
        clear()
        visos_pajamos = 0
        visos_islaidos = 0
        for balansas in biudzetas.__zurnalas:
            if isinstance(balansas, Pajamos):
                visos_pajamos += balansas.suma 
            elif isinstance(balansas, Islaidos):
                visos_islaidos += balansas.suma 
        print(f"Balansas: {visos_pajamos - visos_islaidos} \n")

biudzetas = Biudzetas()

while True:
    print(' 1 - Ataskaitą.\n '   
    '2 - Balansas. \n '
    '3 - Sukurti pajamų įrašą. \n '
    '4 - Sukurti išlaidų įrašą. \n '
    '0 - Išeiti. \n ')
    pasirinkimas = int(input('Pasirinkite operaciją: '))
    

    if pasirinkimas == 1:
        biudzetas.ataskaita()
    elif pasirinkimas == 2:
        biudzetas.balansas()
    elif pasirinkimas == 3:
        pajamu_menu()
    elif pasirinkimas == 4:
        islaidu_menu()
    elif pasirinkimas == 0:
        clear()
        break
    else:
        clear()
        print('Tokio pasirinkimo nėra, prašome bandyti dar kartą.')