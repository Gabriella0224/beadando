#21. Feladat
#A 2520 a legkisebb szám ami maradék nélkül osztható minden számmal 1 és 10 között.
#Írjon programot, amely meghatározza a legkisebb számot ami osztható 1 és N között
#lévő összes számmal. Az implementáció legyen ötletes és hatékony, közel valós időben
#fusson le akár N=20-ra is.

def oszthato(szam,meddig): #létrehozunk egy osztható függvényt ,ami két paramétert kap a vizsgált számot és az N értéket.(1-N)
  for i in range(1,meddig+1):#0-val nem osztunk,nem szorzunk!ezért 1-től indulunk
    if szam % i != 0: #megnézem osztható-e
      return False #ha nem akkor False-al tér vissza
    elif ((i<meddig) and (szam % i == 0)):#ha osztható,de még nem értük el a N számot akkor tovább megyünk.
      continue #menjen tovább a következőre
    else:
      return True #minden egyéb esetben igazzal tér vissza
    #Akkor jutunk ide ,ha nem volt olyan szám amivel nem osztható és elértük az i=N-et!

#print (oszthato(2520,10))
#print (oszthato(12,4))
#print (oszthato(12,5))


n= 10 #megadunk egy N számot és 1 és N között vizsgáljuk,hogy osztható-e mindennel.
legkisebb = n #megadunk egy legkisebb értéket, azért n értéket adunk meg ,mert nem akarjuk feleslegesen számoltatni(10/10=1)
while True: #végtelen ciklust indítunk,mert nem tudjuk hányszor fog végre hajtódni
  if (oszthato(legkisebb, n)): #meghívjuk a függvényt és megvizsgáljuk a számot ,hogy 1 és N között mindennel osztható-e
    print("A", legkisebb, "oszthato minden szammal 1 és ", n, "kozott")#ha True-val tér vissza ,akkor kiíratjuk az eredményt
    break  #a végtelen ciklusból kilépünk
  else: #ha False-al tér vissza függvény akkor bele lép és növeljük a vizsgált szám értékét 1-el)
    legkisebb+=1
