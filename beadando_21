def oszthato(szam,meddig):
  for i in range(1,meddig+1):
    if szam % i != 0:
      return False
    elif ((i<meddig) and (szam % i == 0)):
      continue
    else:
      return True


#print (oszthato(2520,10))
#print (oszthato(12,4))
#print (oszthato(12,5))


n= 10
legkisebb = n
while True:
  if (oszthato(legkisebb, n)):
    print("A", legkisebb, "oszthato minden szammal 1 és ", n, "kozott")
    break
  else:
    legkisebb+=1
