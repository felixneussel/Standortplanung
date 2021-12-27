"""Ungewichtete 1-Centerprobleme in der Ebene"""
def transformieren(punkt):
    return (punkt[0]+punkt[1], -punkt[0]+punkt[1])

def rücktransformieren(punkt):
    return (0.5*(punkt[0]-punkt[1]), 0.5*(punkt[0]+punkt[1]))

def solve_l1(standorte):
    standorte_trans = []
    for s in standorte:
        standorte_trans.append(transformieren(s))
    print("transformierte Koordinaten:", standorte_trans)

    min_x1 = min(standorte_trans, key=lambda a:a[0])[0]
    max_x1 = max(standorte_trans, key=lambda a:a[0])[0]
    min_x2 = min(standorte_trans, key=lambda a:a[1])[1]
    max_x2 = max(standorte_trans, key=lambda a:a[1])[1]
    min_x1_trans = min_x1
    max_x1_trans = max_x1
    min_x2_trans = min_x2
    max_x2_trans = max_x2
    
    print("Umschreibendes Rechteck (Nicht rücktransformiert):", min_x1, min_x2, max_x1, max_x2)
    print("Umschreibendes Rechteck (rücktransformiert):", rücktransformieren((min_x1_trans,min_x2_trans)), rücktransformieren((max_x1_trans,max_x2_trans)))

    # falls transformierte Koordinaten mit einem Quadrat überdeckt werden, ist Mittelpunkt optimaler Standort:
    if abs(min_x1-max_x1) == abs(min_x2-max_x2):
        x = [(min_x1+max_x1)/2, (min_x2+max_x2)/2]
        print("Optimaler Standort (Quadrat) (noch nicht ruecktransformiert):", x)
        print("Optimaler Standort (Quadrat) (ruecktransformiert):", rücktransformieren(x))
        return

    # falls Rechteck "flach", nach oben und unten ausdehnen:
    if abs(min_x1-max_x1) > abs(min_x2-max_x2):
        # nach oben ausdehnen:
        max_x2_neu = max_x2 + (abs(min_x1-max_x1) - abs(min_x2-max_x2))
        xo = [(min_x1+max_x1)/2, (min_x2+max_x2_neu)/2]
        # nach unten ausdehnen:
        min_x2_neu = min_x2 - (abs(min_x1-max_x1) - abs(min_x2-max_x2))
        xu =  [(min_x1+max_x1)/2, (min_x2_neu+max_x2)/2]
        print("Nicht rücktransformierte Optimale Standorte liegen zwischen", xo, "und", xu)
        print("Rücktransformierte Optimale Standorte liegen zwischen", rücktransformieren(xo), "und", rücktransformieren(xu))
        return

    # falls Rechteck "schmal", nach links und rechts zu Quadrat ausdehnen:
    # nach rechts ausdehnen:
    max_x1_neu = max_x1 + (abs(min_x2-max_x2) - abs(min_x1-max_x1))
    xr = [(min_x1+max_x1_neu)/2, (min_x2+max_x2)/2]
    # nach links ausdehnen:
    min_x1_neu = min_x1 - (abs(min_x2-max_x2) - abs(min_x1-max_x1))
    xl = [(min_x1_neu+max_x1)/2, (min_x2+max_x2)/2]
    print("Nicht rücktransformierte Optimale Standorte liegen zwischen", xl, "und", xr)
    print("Optimale Standorte liegen zwischen", rücktransformieren(xl), "und", rücktransformieren(xr))
    return

def solve_l_unendlich(standorte):
    """Wie solve_l1, nur ohne Koordinatentransformation"""

    min_x1 = min(standorte, key=lambda a:a[0])[0]
    max_x1 = max(standorte, key=lambda a:a[0])[0]
    min_x2 = min(standorte, key=lambda a:a[1])[1]
    max_x2 = max(standorte, key=lambda a:a[1])[1]
    print("Umschreibendes Rechteck:", min_x1, min_x2, max_x1, max_x2)

    # falls transformierte Koordinaten mit einem Quadrat überdeckt werden, ist Mittelpunkt optimaler Standort:
    if abs(min_x1-max_x1) == abs(min_x2-max_x2):
        x = [(min_x1+max_x1)/2, (min_x2+max_x2)/2]
        print("Optimaler Standort (Quadrat):", x)
        return

    # falls Rechteck "flach", nach oben und unten ausdehnen:
    if abs(min_x1-max_x1) > abs(min_x2-max_x2):
        # nach oben ausdehnen:
        max_x2_neu = max_x2 + (abs(min_x1-max_x1) - abs(min_x2-max_x2))
        xo = [(min_x1+max_x1)/2, (min_x2+max_x2_neu)/2]
        # nach unten ausdehnen:
        min_x2_neu = min_x2 - (abs(min_x1-max_x1) - abs(min_x2-max_x2))
        xu =  [(min_x1+max_x1)/2, (min_x2_neu+max_x2)/2]
        print("Optimale Standorte liegen zwischen", xo, "und", xu)
        return

    # falls Rechteck "schmal", nach links und rechts zu Quadrat ausdehnen:
    # nach rechts ausdehnen:
    max_x1_neu = max_x1 + (abs(min_x2-max_x2) - abs(min_x1-max_x1))
    xr = [(min_x1+max_x1_neu)/2, (min_x2+max_x2)/2]
    # nach links ausdehnen:
    min_x1_neu = min_x1 - (abs(min_x2-max_x2) - abs(min_x1-max_x1))
    xl = [(min_x1_neu+max_x1)/2, (min_x2+max_x2)/2]
    print("Optimale Standorte liegen zwischen", xl, "und", xr)
    return

"""    
beispiel = [(4,12), (8,2), (14,10), (2,3), (14,4)]
solve_l1(beispiel)

beispiel2 = [(1,1), (2,1), (1,2), (2,2), (1.5,1.5)]
beispiel3 = [(0,0), (1,0), (0,2), (1,2)]
solve_l_unendlich(beispiel3)
"""

punkte = [(4,6),(8,10),(11,4),(15,8)]
solve_l1(punkte)

