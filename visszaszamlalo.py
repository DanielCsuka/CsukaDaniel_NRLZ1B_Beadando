import time
from tkinter import *
from tkinter import messagebox

# ablak létrehozása
ablak = Tk()

# ablak méretének beállítása
ablak.geometry('270x200')
ablak.minsize(width=200, height=190)
ablak.maxsize(width=350, height=300)

# ablak nevének beállítása
ablak.title('Visszaszámláló')

# változók beállítása
perc = StringVar()
masodperc = StringVar()

# 00-t beállítjuk alapértéknek
perc.set('00')
masodperc.set('00')

# 1970 január 1-je óta eltelt másodpercek
masodpercek = time.time()
# másodperceket átalakítja a mostani idő szerint
akt_ido = f'Aktuális idő: {time.ctime(masodpercek)}'

# Az Entry-vel bekérjük a felhasználótól a percet és/vagy a másodpercet
# place-el el tudjuk pontosan helyezni az ablakon
percBevitel = Entry(ablak, width=3, font=('Arial', 30, ''), textvariable=perc)
percBevitel.place(x=65, y=40)

mpBevitel = Entry(ablak, width=3, font=('Arial', 30, ''), textvariable=masodperc)
mpBevitel.place(x=130, y=40)

pontos_ido = Label(ablak, text=akt_ido, foreground='blue', font=('Arial', 11, ''))
pontos_ido.place(x=5, y=10)

def bevitel():
    try:
        # a felhasználótól kapott adatokat a temp-ben tároljuk
        temp = int(perc.get()) * 60 + int(masodperc.get())
    except (ValueError):
            messagebox.showinfo('Hiba!', 'Számot írj be!',)
    while temp > -1:
        percek, mpk = divmod(temp, 60)

        # formátum
        perc.set('{0:2d}'.format(percek))
        masodperc.set('{0:2d}'.format(mpk))

        # updateljük az ablakot minden alkalommal amikor vált a számláló
        ablak.update()
        time.sleep(1)

        # ha eléri a 0-t kiírjuk, hogy lejárt az idő
        if (temp == 0):
            messagebox.showinfo('Visszaszámláló', 'Lejárt az idő!')

        # temp értéke minden másodpercben egyet csökken
        temp -= 1

def informacio():
    messagebox.showinfo('Információ', 'Visszaszámláló feladat: Grafikus felületen a felhasználó megadhat percet '
                                      'és/vagy másodpercet, ahonnan a program vissza fog számolni és amint ez letelt kiírja, hogy lejárt az idő.')

# gombok
inditas_gomb = Button(ablak, text='Visszaszámlálás indítása', bd='5', command=bevitel)
inditas_gomb.place(x=70, y=120)
kilepes_gomb = Button(ablak, text='Kilépés', bd='5', command=ablak.destroy)
kilepes_gomb.place(x=70, y=150)

# menüsor
menusor = Menu(ablak)
menu = Menu(menusor)
menu.add_command(label='Információ', command=informacio)
menu.add_command(label='Kilépés', command=ablak.destroy)
menusor.add_cascade(label='Menü', menu=menu)

ablak.config(menu=menusor)

# végtelen loop
ablak.mainloop()