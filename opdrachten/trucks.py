from z3 import *

# Stel je voor, je bent de trotse eigenaar van een bruisend distributiecentrum. Je hebt acht vrachtwagens tot je beschikking, waarvan drie speciale koeltrucks zijn, 
# perfect voor het vervoeren van bevroren lekkernijen. Iedere vrachtwagen kan 8000 kg en maximaal 8 pallets meenemen. Vandaag heb je een interessante uitdaging: 
# een klant heeft een nogal unieke bestelling geplaatst.

# Hier is wat je moet versturen:
    # • Cola: 10 pallets, elk pallet weegt 2500 kg.
    # • Ijsjes: 8 pallets, elk pallet weegt 1000 kg. Deze moeten koel blijven, dus alleen koeltrucks voor deze ijsjes!
    # • Koekjes: 20 pallets, elk weegt 200 kg.
    # • Mentos: Zoveel mogelijk pallets, elk weegt 400 kg. De klant kan er geen genoeg van krijgen!
    # • Kaviaar: 4 pallets, elk weegt 700 kg. Vanwege de hoge waarde, mag je slechts één pallet per vrachtwagen vervoeren.

# Opdracht a)
# Jouw missie, mocht je die accepteren, is om deze goederen zo efficiënt mogelijk over je vrachtwagens te verdelen. Onthoud dat de ijsjes koel moeten blijven en dat 
# je maar één pallet kaviaar per vrachtwagen mag vervoeren. De rest van de goederen kan naar eigen inzicht worden verdeeld, zolang je maar zoveel mogelijk Mentos meeneemt.

# opdracht b)
# Nadat een van je collega’s je een video laat zien waarin mentos in een fles cola wordt gedaan wil je deze niet meer samen in 1 vrachtwagen vervoeren. Bereken nu hoeveel 
# pallets mentos je nog meekrijgt.

# Truck loading
s = Optimize()

# Specificeer het aantal pallets van ieder product (gegeven dat 0, 1, en 2 koeltrucks zijn)
cola = [Int(f'cola_{i}') for i in range(8)]
ijsjes = [Int(f'ijsjes_{i}') for i in range(8)]
koekjes = [Int(f'koekjes_{i}') for i in range(8)]
kaviaar = [Int(f'kaviaar_{i}') for i in range(8)]
mentos = [Int(f'mentos_{i}') for i in range(8)]

# Intialiseer het aantal van iedere pallet

# totaal gewicht <= 8000

# totaal aantal per truck <= 8

# maar 1 kaviaar per truck

# geen ijsjes in iedere truck

# Geen enkele truck mag een negatief aantal van een pallet hebben

s.maximize(Sum(mentos))

if s.check() == sat:
    m = s.model()
    for i in range(8):
        aKoekjes = m.eval(koekjes[i]).as_long() if m.eval(koekjes[i]) is not None else 0
        aCola = m.eval(cola[i]).as_long() if m.eval(cola[i]) is not None else 0
        aIjsjes = m.eval(ijsjes[i]).as_long() if m.eval(ijsjes[i]) is not None else 0
        aKaviaar = m.eval(kaviaar[i]).as_long() if m.eval(kaviaar[i]) is not None else 0
        aMentos = m.eval(mentos[i]).as_long() if m.eval(mentos[i]) is not None else 0

        totaal_gewicht = aKoekjes * 200 + aCola * 2500 + aIjsjes * 1000 + aKaviaar * 700 + aMentos * 400

        print(
            f'truck {i + 1}, met {aKoekjes} koekjes, {aCola} cola, {aIjsjes} ijsjes, {aKaviaar} kaviaar, {aMentos} mentos. Totaal gewicht: {totaal_gewicht}')
    total_mentos = sum(m[mentos[i]].as_long() for i in range(8))
    print(f'Aantal mentos pallets te verkopen: {total_mentos}')
else:
    print('Kon geen correcte planning vinden')