from algemene_functies import mijn_functie_2

def aanbieding_1 (smaak, prijs, korting) : 
    korting_1 = prijs * korting
    korting_2 = prijs - korting_1
    text_1 = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro, naar {korting_2} euro"
    return text_1

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal  = sum(inkomsten)
    totaal_btw = totaal * btw
    text_2 = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal_btw} euro btw betaald dient te worden."
    return text_2

btw_procent = 0.09
inkomen_per_dag = 220, 430, 125, 160, 205, 90, 345
inkomen_totaal = inkomsten_totaal(inkomen_per_dag, btw_procent)

print(inkomen_totaal)

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return laagste, hoogste

laagste_en_hoogste = 220, 430, 125, 160, 205, 90, 345
uitkomst = laag_en_hoog(laagste_en_hoogste)
print(uitkomst)

def gemiddelde(mijn_lijst):
    gem1 = sum(mijn_lijst)
    gem2 = len(mijn_lijst)
    gem3 = gem1 / gem2
    tekst_3 = f"De gemiddelde inkomsten deze week zijn {gem3} euro"
    return tekst_3

gemiddelde_inkomen = 220, 430, 125, 160, 205, 90, 345
gemid = gemiddelde(gemiddelde_inkomen)
print (gemid)

def meervoudig(invoer_lijst):
    avg_lijst = laag_en_hoog(meervoudig_lijst)
    return avg_lijst

meervoudig_lijst = 10,5,3,2,1,2,9
uitkomst2 = laag_en_hoog(meervoudig_lijst)
print(uitkomst2)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer