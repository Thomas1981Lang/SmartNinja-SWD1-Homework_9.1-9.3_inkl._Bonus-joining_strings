import math

# coding=utf-8
# Implementiere einen Rentenrechner
# Anfangskapital: 100
# Zinsen: 6%
# Laufzeit: Jahre
# Formel für die Zinseszinsrechnung: Anfangskapital * ((1+(Zinsatz/100)) ^ jeweiligen Jahre)
# Anfangskapital*math.pow(Zinsen,1)

anfangskapital = test = test2 = 100

zins = 6
veranlagungszeitraum = 5
for i in range(1, veranlagungszeitraum + 1):
    # Version 1:
    print('Version 1: ', anfangskapital * math.pow(((zins / 100) + 1), i))

    # Version 2:
    test = test * ((zins / 100) + 1)
    print('Version 2: ', test)

    # Version 3:
    test2 = test2 + (test2 / 100 * zins)
    print('Versuch 3: ', test2)

"""
Ergebnis:
Anfangskapital:  100
Zinssatz:  6.0
Veranlagungszeitraum:  5
Kapital im Jahr 1 : 106.0
Kapital im Jahr 2 : 112.36
Kapital im Jahr 3 : 119.1016
Kapital im Jahr 4 : 126.247696
Kapital im Jahr 5 : 133.82255776
"""
