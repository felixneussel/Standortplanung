def zielfunktion_l1(kandidat, kunden):
    summe = 0
    for k in kunden:
        summe += abs(k[0]-kandidat[0])*k[2]*2 + abs(k[1]-kandidat[1])*k[2]*2
    return summe

def solve_l1(standorte):
    """Loest ein 1-Medianproblem mit l1-Metrik fuer eine Liste 
    von Kundenstandorten ('standorte'), die in der Form (x1, x2, w) gegeben sind."""
    summe_gewichte = 0
    for s in standorte:
        summe_gewichte += s[2]
    
    # ueberpruefen, ob Dominanzkriterium bereits fuer einen Stadort erfuellt ist:
    for s in standorte:
        if s[2] >= summe_gewichte/2:
            print("Optimal Location (Dominance criterion):", s, ", Objective value:", zielfunktion_l1(s, standorte))
            return s

    summe_x1 = 0
    standorte.sort()
    x1 = 0
    for s in standorte:
        summe_x1 += s[2]
        if summe_x1 >= summe_gewichte/2:
            x1 = s[0]
            break

    summe_x2 = 0
    standorte.sort(key=lambda a: a[1])
    x2 = 0
    for s in standorte:
        summe_x2 += s[2]
        if summe_x2 >= summe_gewichte/2:
            x2 = s[1]
            break
    
    optimaler_standort = (x1,x2)
    print("Optimal Location:", optimaler_standort, ", Objective function:", zielfunktion_l1(optimaler_standort, standorte) )
    return optimaler_standort


klausur = [(4,1,2200),(8,3,1800),(10,1,4500),(13,9,2500)]

print(solve_l1(klausur))






"""
kundenstandorte = [(10,3,1), (6,5,1.5), (10,7,0.75), (12,7,1)]
pubsundhafen = [(5,2,3), (8,5,5), (3,7,0), (1,2,2)]
pubsundhafen2 = [(5,2,2), (8,5,0), (3,7,5), (1,2,2)]
vorlesung = [(1,4,2),(2,6,3),(5,1,1),(4,2,1),(6,5,2)]
uebung = [(6,5,3),(10,3,2),(12,7,2),(10,7,1.5)]
onlinetest = [(2,2,5),(10,0,2),(5,6,4),(0,10,1),(4,6,4),(9,9,7)]
depot_1 = [(7,5,1),(9,8,3),(4,7,0),(2,6,3)]
depot_2 = [(7,5,3),(9,8,0),(4,7,2),(2,6,2)]
"""
#Hier aufpassen. Es wird automatisch fue Hin und Rueckweg berechnet. D.h. wenn Hin und Rueckweg schon
#in den Gewichten beruecksichtigt sind, muss das Ergebnis durch zwei geteilt werden.
#solve_l1(kundenstandorte)


#punkte = [(10,4),(9,5),(10,6),(11,5)]
#restricted(punkte,uebung)
    
