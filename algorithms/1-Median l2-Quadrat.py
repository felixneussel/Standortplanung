import math

def zielfunktion(kandidat, kunden):
    summe = 0 
    for k in kunden:
        #summe += (kandidat[0]-k[0])*(kandidat[0]-k[0])*k[2] + (kandidat[1]-k[1])*(kandidat[1]-k[1])*k[2]
        summe += k[2] * math.sqrt((kandidat[0]-k[0])*(kandidat[0]-k[0]) + (kandidat[1]-k[1])*(kandidat[1]-k[1]))
    return summe

def solve(standorte):
    # Dominanzkriterium überprüfen:
    summe_gewichte = 0
    for s in standorte:
        summe_gewichte += s[2]
    for s in standorte:
        if s[2] >= summe_gewichte/2:
            print("optimaler Standort (Dominanz):", s, "Zielfunktionswert:", zielfunktion(s, standorte))
            return
    
    # Schwerpunkt ist optimaler Punkt:
    summe_x1 = 0
    for s in standorte:
        summe_x1 += s[0]*s[2]
    summe_x2 = 0
    for s in standorte:
        summe_x2 += s[1]*s[2]
    x = [round(summe_x1/summe_gewichte,2), round(summe_x2/summe_gewichte,2)]
    print("Optimaler Standort:", x,  ", Zielfunktionswert:", zielfunktion(x, standorte) )


#ACHTUNG, MOMENTAN WIRD ALS ZIELFUNKTION DIE NICHT QUADRIERTE EUKLIDISCHE METRIK GENUTZT, NUR FUER HINWEG

beispiel = [(5,2,6),(5,4,7),(6,10,4),(1,5,6),(6,5,4)]
solve(beispiel)