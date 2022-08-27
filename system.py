class System():

    def privitani(self):
        print(  "----------------------------------------\n" +
                "---- System pro evidenci pojistencu ----\n" +
                "----------------------------------------")

    def moznosti(self):
        print(  "\nMenu\n" +
                "1 - Pridat klienta \n" +
                "2 - Vypsat vsechny klienty \n" +
                "3 - Vyhledat klienta \n" +
                "4 - Konec \n")

    def vycistit(self):
        print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")

    def vypis(self, jmeno, prijmeni, telefonni_cislo, vek):
        return f"{jmeno}\t {prijmeni}\t {telefonni_cislo}\t {vek}"

    def neplatna_vstupni_data(self):
        return "\nChybna vstupni data!!\nZkuste to znova :)\n"

    def rozlouceni(self):
        return "\nHezky zbytek dne :)"

    def nenalezen(self, jmeno, prijmeni):
        return f"\n- {jmeno}\t {prijmeni}\t\t Nenalezen :( -"
