from system import System

sys = System()
klienti = []   #[]
case = '0'     #str
sys.privitani()

while case != '4':
    sys.moznosti()
    case = input("Zvolte akci a potvrdte enterem: ")

    if case == '1':
        while 1:
            sys.vycistit()
            jmeno = input("Zadejte jmeno: ")
            prijmeni = input("Zadejte prijimeni: ")
            if jmeno == '' or prijmeni == '':
                print(sys.neplatna_vstupni_data())
            else:
                break;
        while 1:
            sys.vycistit()
            try:
                telefonni_cislo = int(input("Zedejte telefon: ")) #musi byt typu int
                break;
            except:
                print(sys.neplatna_vstupni_data())
        while 1:
            sys.vycistit()
            try:
                vek = int(input("Zadejte vek: ")) #musi byt typu int
                break;
            except:
                print(sys.neplatna_vstupni_data())
        klienti.append([jmeno, prijmeni, telefonni_cislo, vek]) #prida klienta

    elif case == '2':
        sys.vycistit()
        for i in range(len(klienti)):
            print(sys.vypis(klienti[i][0], klienti[i][1], klienti[i][2], klienti[i][3]))

    elif case == '3':
        sys.vycistit()
        zaznam = False
        hledane_jmeno = str(input("Zadejte hledane jmeno: "))
        hledane_prijmeni = str(input("Zadejte hledane prijmeni: "))
        for i in range(len(klienti)):
            if hledane_jmeno == klienti[i][0] and hledane_prijmeni == klienti[i][1]:
                print(sys.vypis(klienti[i][0], klienti[i][1], klienti[i][2], klienti[i][3]))
                zaznam = True
        if zaznam is False: #Nenasel klienta
            print(sys.nenalezen(hledane_jmeno, hledane_prijmeni))
    elif case == '4':
        print(sys.rozlouceni())

    else:
        print(sys.neplatna_vstupni_data())
    input("OK")
    sys.vycistit()
sys.rozlouceni()