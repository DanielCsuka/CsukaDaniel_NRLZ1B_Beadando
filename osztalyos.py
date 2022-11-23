import kalendar
from random import *
from datetime import date

# osztály
class adatok():
    nev = ''
    szuletesnap = None
    szuletesi_hely = ''

    def __init__(self):
        self.nev = 'név'
        self.szuletesnap = '1800.01.01'
        self.szuletesi_hely = 'hely'

 # hány napja született függvény, a random dátumból kivonja a mostani dátumot
def hany_napja_szuletett():
    randomdatum = date(year=randomev, month=randomho, day=randomnap)
    aktualdatum = date(year=2022, month=11, day=24)
    napok = randomdatum - aktualdatum
    return napok

# random
randomev = randrange(1800, 2021)
randomho = randrange(1, 12)
randomnap = randrange(1, 31)

# értékadás, kiiratás
if __name__ == '__main__':
    elso = adatok()
    elso.nev = 'Név: Kossuth Lajos'
    elso.szuletesnap = f'Születésnap: {randomev}.{randomho}.{randomnap}.'
    elso.szuletesi_hely = 'Születési hely: Dunaújváros'

    print(elso.nev)
    print(elso.szuletesnap)
    print('Ennyi napja született:', hany_napja_szuletett())
    print(kalendar.kalendarium(randomev, randomho, randomnap))
    print(elso.szuletesi_hely)