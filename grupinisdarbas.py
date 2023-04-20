# Komandinis darbas - biudžeto programėlė
# Klasės
# Irasas (abstraktus)

# savybė suma
# savybė komentaras
# Islaidos(Irasas)

# savybė gavejas
# Pajamos(Irasas)

# savybė siuntejas
# Biudzetas

# savybe zurnalas: sąrašas įrašų
# Biudzetas turi turėti metodus:

# ataskaitai
# balansas
# pajamų įrašo sukūrimas ir įtraukimui į žurnalą
# išlaidų įrašo sukūrimas ir įtraukimui į žurnalą
# Programos meniu ir funkcionalumą galite įgyvendinti tiek per klasę, tiek pagrindinėje programoje.

irasu_sarasas = []

class Irasas():
    def __init__(self, suma, komentaras):
        self.suma = suma
        self.komentaras = komentaras


class Islaidos(Irasas):
    def __init__(self, gavejas, suma, komentaras):
        self.gavejas = gavejas
        self.suma = suma
        self.komentaras = komentaras


class Pajamos(Irasas):
    def __init__(self, siuntejas, suma, komentaras):
        self.siuntejas = siuntejas
        self.suma = suma
        self.komentaras = komentaras


class Biudzetas():
    def __init__(self, ataskaita, balansas, suma, komentaras):
        self.ataskaita = ataskaita
        self.balansas = balansas
        self.suma = suma
        self.komentaras = komentaras




