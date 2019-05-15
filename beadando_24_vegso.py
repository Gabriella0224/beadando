#24
#Írjon programot, amely összead két, kettes és tízes közötti tetszőleges számrendszerben
#ábrázolt számot, majd ugyan abban a számrendszerben megadja a művelet eredményét!
#A program a standard bementről olvassa be a számrendszert és a két számot!
def val(c):                           #átalakít stringből számba (stringként kapja meg a számot)
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def reVal(num):                        #visszalakít számból stringbe
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))


def toDeci(str, base):              #átkonvertálás 10-es számrendszerbe
    llen = len(str)
    power = 1
    num = 0


    for i in range(llen - 1, -1, -1):       #fordítva végig megy a karaktereken

        if val(str[i]) >= base:         #ellenőrzés
            print('Invalid Number')     #ha érvénytelen a szám
            return -1                                                      ###itt művelet ügyileg történik meg a számrendszerbe való átváltás
        num += val(str[i]) * power      #ha érvényes
        power = power * base            #a hatvány szorzódik a bázissal
    return num                          #visszatér az összeggel


def fromDeci(res, base, inputNum):          #visszaalakítja az eredeti számrendszerbe
    index = 0
    while (inputNum > 0):                   #magát az összeadás műveletet a 10-es számrendszerben végzi el
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)


    res = res[::-1]

    return res


a = int(input('Hanyas számrendszer? (számmal)'))    #számként olvasom be a felhasználótól
b = input('Első szám: ')                            #stringként olvasom be a felhasználótól
c = input('Masodik szam: ')                         # -||-

elso=toDeci(b,a)                  #meghívom a függvényt
masodik=toDeci(c,a)
res=""
print("Az összeg ebben a számrendszerben ",fromDeci(res,a,elso+masodik))
