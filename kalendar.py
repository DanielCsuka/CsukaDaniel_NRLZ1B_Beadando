import calendar

def kalendarium(ev, ho, nap):
    yy = ev    # év
    mm = ho    # hónap
    dd = nap   # nap

    # kalendár kiírása
    calendar.format(cols='', colwidth=100, spacing=100)
    print(calendar.month(yy, mm, dd))


