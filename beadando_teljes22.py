#Két négyjegyű szám szorzataként előállítható legnagyobb palindrom szám.

def palindrom(szam): #megnézzük,hogy palindrom-e a szám
  szam = str(szam) #stringgé konvertaljuk,mert akkor lehet vele str muveleteket vegezni
  rev_szam = szam[::-1]  #megfordítjuk ,::->[mettől:meddig:lépésköz] -1 vége
  rev_szam = int(rev_szam) #int-é konvertáljuk mindkettőt
  szam = int(szam)
  if szam == rev_szam: # megnézem,hogy ugyanaz-e
    return True #ha ugyanaz akkor palindrom,True
  else:
    return False #különben nem palindrom

pal1 = 9999
pal2 = 9999

while True: #végtelen ciklust indítunk el
  pal = pal1 * pal2 #pall nevű változót hozunk létre,a vizsgalt szamunk lesz,a két számot összeszorozzuk
  if palindrom(pal): #ha a vizsgált szám palindrom,akkor örülünk és kilépünk a breakkel
    print ("Két négyjegyű szám szorzataként előállítható legnagyobb palindrom szám: ", pal, "=", pal1, "*" , pal2)
    break
  elif pal1 > pal2: #ha a pl1>pal2 akkor a pal2 értékét csökkentjük 1-el
    pal2 = pal2-1
  else: #különben a pal1 értékét csökkentjük 1-el
    pal1 = pal1-1
