# Vektor (erster Eintrag, zweiter Eintrag, Gewicht)
import math
def gamma(kandidat, rest):
    summe = [0,0]
    for vektor in rest:
        summe[0] = summe[0] + vektor[2]*(kandidat[0]-vektor[0])/entfernung(kandidat, vektor)
        summe[1] = summe[1] + vektor[2]*(kandidat[1]-vektor[1])/entfernung(kandidat, vektor)
    return entfernung(summe, [0,0])

def entfernung(a,b):
    return math.sqrt(math.pow((a[0]-b[0]),2) + math.pow((a[1]-b[1]),2))

def zielfunktion(kandidat, rest):
    kosten = 0
    for vektor in rest:
        kosten += entfernung(vektor, kandidat)*vektor[2]
    return kosten

def iteration(kandidat, rest):
    zielfunktionswertalt = zielfunktion(kandidat, rest)
    summeO1 = 0
    summeU1 = 0
    summeO2 = 0
    summeU2 = 0
    for vektor in rest:
        summeO1 += vektor[2]*vektor[0]/entfernung(kandidat, vektor)
        summeU1 += vektor[2]*1/entfernung(kandidat, vektor)
        summeO2 += vektor[2]*vektor[1]/entfernung(kandidat, vektor)
        summeU2 += vektor[2]*1/entfernung(kandidat, vektor)
    
    kandidat[0] = summeO1/summeU1
    kandidat[1] = summeO2/summeU2
    zielfunktionswertneu = zielfunktion(kandidat, rest)
    abweichung = (zielfunktionswertalt-zielfunktionswertneu)/zielfunktionswertalt
    return abweichung, kandidat
    
def weiszfeld(standorte, delta):
    # überprüfe, ob einer der existierenden Standorte schon das verschärfte Dominanzkriterium erfüllt:
    for s in standorte:
        standorte.remove(s)
        if gamma(s, standorte) <= s[2]:
            print("Optimaler Standort (Dominanz):", s, ", Zielfunktionswert:", zielfunktion(s, standorte))
            return
        standorte.append(s)

    # Schwerpunkt berechnen
    summe_gewichte = 0
    for s in standorte:
        summe_gewichte += s[2]
    summe_x1 = 0
    for s in standorte:
        summe_x1 += s[0]*s[2]
    summe_x2 = 0
    for s in standorte:
        summe_x2 += s[1]*s[2]
    x0 = [summe_x1/summe_gewichte, summe_x2/summe_gewichte]
    print("Start mit Schwerpunkt x0 =", x0,  ", Zielfunktionswert:", zielfunktion(x0, standorte) )

    i = 1
    a, k = iteration(x0, standorte)
    print("Iteration", i, ", x =", k, "Zielfunktionswert:", zielfunktion(k, standorte), ", delta:", a)
    while a > delta:
        i += 1
        a, k = iteration(k, standorte)
        print("Iteration", i, ", x =", k, "Zielfunktionswert:", zielfunktion(k, standorte), ", delta:", a)


a = [18,2,6]
b = [4,0,2]
c = [6,20,7]
d = [12,18,4]

beispiel = [a,b,c,d]
weiszfeld(beispiel, 0.005)

# gegebenen Punkt eine Iteration mit Weiszfeld verbesern:
print(iteration([11,12], beispiel))







