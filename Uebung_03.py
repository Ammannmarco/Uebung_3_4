#Aufgabe 1: Vererbung
#Schreiben Sie die Klassen "Dreieck", "Rechteck", "Kreis" und "Polygon"
#Diese Klassen werden von folgender Python Klasse vererbt:
#class Figur:
#    def __init__(self):
#        self.name = "Figur"

#    def Umfang(self):
#        return 0
    
#    def __str__(self):
#        return self.name
    
#• Das Attribut "name" ist eine Zeichenkette welche den Namen des jeweiligen Objektes enthält.
#• Die Methode "Umfang" soll für die jeweilige Figur korrekt implementiert werden
#• Finden Sie geeignete Konstruktoren um die Figuren zu konstruieren
#• __str__ soll die Figur mit allen Koordinaten sinnvoll beschreiben, z.B:
#    o "Kreis M=(2.3,4.2) r=3.4"
#    o "Rechteck (0,0) – (10,15)"

#Hinweise:
#• Die Figuren sind 2D
#• Verwenden Sie eine Klasse Punkt („Point“) um die Koordinaten der Figuren zu verwalten.
#• Die Seiten bei Rechteck sind parallel zur jeweiligen Koordinaten-Achse.
#• Wählen Sie geeignete Konstruktoren, z.B. bei Polygon sollen beliebig viele Ecken unterstützt werden.


import math  # Importiere das math-Modul, um mathematische Funktionen zu verwenden

class Figur:  # Definiere eine Klasse "Figur"
    def __init__(self, name):  # Konstruktor, der den Namen der Figur initialisiert
        self.name = name  # Initialisiere das Attribut "name" mit dem übergebenen Namen

    def umfang(self):  # Methode zur Berechnung des Umfangs
        return 0  # Rückgabe des Umfangs, Standardwert für Figuren ohne spezifische Umfangsberechnung

    def flaeche(self):  # Methode zur Berechnung der Fläche
        return 0  # Rückgabe der Fläche, Standardwert für Figuren ohne spezifische Flächenberechnung

    def __str__(self):  # Methode zur Darstellung der Figur als Zeichenkette
        return self.name  # Rückgabe des Namens der Figur als Zeichenkette


class Punkt(Figur):  # Klasse Punkt erbt von Figur
    def __init__(self, x, y):  # Konstruktor für die Klasse Punkt
        super().__init__("Punkt")  # Rufe den Konstruktor der Elternklasse mit dem Namen "Punkt" auf
        self.x = x  # Initialisiere die x-Koordinate des Punkts
        self.y = y  # Initialisiere die y-Koordinate des Punkts

    def distanz(self, other):  # Methode zur Berechnung der Distanz zwischen zwei Punkten
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)  # Berechne die euklidische Distanz

    def __str__(self):  # Methode zur Darstellung des Punkts als Zeichenkette
        return f"Punkt(x = {self.x}, y = {self.y})"  # Rückgabe der Koordinaten des Punkts als Zeichenkette

# Ähnliche Erklärungen gelten auch für die folgenden Klassen (Kreis, Dreieck, Rechteck, Polygon).
# Die Methoden __init__, umfang und __str__ sind spezifisch für jede Klasse implementiert.

class Kreis(Figur):  # Definiere eine Klasse "Kreis", die von der Klasse "Figur" erbt
    def __init__(self, mittelpunkt, radius):  # Konstruktor für die Klasse "Kreis"
        super().__init__("Kreis")  # Rufe den Konstruktor der Elternklasse mit dem Namen "Kreis" auf
        self.mittelpunkt = mittelpunkt  # Initialisiere das Attribut "mittelpunkt" mit dem übergebenen Wert
        self.radius = radius  # Initialisiere das Attribut "radius" mit dem übergebenen Wert

    def flaeche(self):  # Methode zur Berechnung der Fläche des Kreises
        return self.radius ** 2 * math.pi  # Berechne die Fläche des Kreises (π * r^2)

    def umfang(self):  # Methode zur Berechnung des Umfangs des Kreises
        return self.radius * 2 * math.pi  # Berechne den Umfang des Kreises (2 * π * r)

    def __str__(self):  # Methode zur Darstellung des Kreises als Zeichenkette
        return f"Kreis Mittelpunkt = {self.mittelpunkt}, r = {self.radius}"  # Gib eine lesbar formatierte Zeichenkette zurück

class Dreieck(Figur):  # Definiere eine Klasse "Dreieck", die von der Klasse "Figur" erbt
    def __init__(self, A, B, C):  # Konstruktor für die Klasse "Dreieck"
        super().__init__("Dreieck")  # Rufe den Konstruktor der Elternklasse mit dem Namen "Dreieck" auf
        self.A = A  # Initialisiere das Attribut "A" mit dem übergebenen Wert
        self.B = B  # Initialisiere das Attribut "B" mit dem übergebenen Wert
        self.C = C  # Initialisiere das Attribut "C" mit dem übergebenen Wert

    def umfang(self):  # Methode zur Berechnung des Umfangs des Dreiecks
        return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.A)  # Berechne die Summe der Seitenlängen

    def __str__(self):  # Methode zur Darstellung des Dreiecks als Zeichenkette
        return f"Dreieck {self.A},{self.B},{self.C}"  # Gib eine lesbar formatierte Zeichenkette zurück

class Rechteck(Figur):  # Definiere eine Klasse "Rechteck", die von der Klasse "Figur" erbt
    def __init__(self, Pmin, Pmax):  # Konstruktor für die Klasse "Rechteck"
        super().__init__("Rechteck")  # Rufe den Konstruktor der Elternklasse mit dem Namen "Rechteck" auf
        self.Pmin = Pmin  # Initialisiere das Attribut "Pmin" mit dem übergebenen Wert
        self.Pmax = Pmax  # Initialisiere das Attribut "Pmax" mit dem übergebenen Wert

    def umfang(self):  # Methode zur Berechnung des Umfangs des Rechtecks
        return 2 * abs(self.Pmax.x - self.Pmin.x) + 2 * abs(self.Pmax.y - self.Pmin.y)  # Berechne den Umfang

    def __str__(self):  # Methode zur Darstellung des Rechtecks als Zeichenkette
        return f"Rechteck Punkte = {self.Pmin}, {self.Pmax}"  # Gib eine lesbar formatierte Zeichenkette zurück

class Polygon(Figur):  # Definiere eine Klasse "Polygon", die von der Klasse "Figur" erbt
    def __init__(self, Punktliste):  # Konstruktor für die Klasse "Polygon"
        super().__init__("Polygon")  # Rufe den Konstruktor der Elternklasse mit dem Namen "Polygon" auf
        self.pl = Punktliste  # Initialisiere das Attribut "pl" mit der übergebenen Punktliste

    def umfang(self):  # Methode zur Berechnung des Umfangs des Polygons
        s = 0  # Initialisiere die Summe der Seitenlängen mit 0
        for i in range(0, len(self.pl) - 1):  # Iteriere über die Liste der Punkte
            l1 = self.pl[i]  # Aktueller Punkt
            l2 = self.pl[i + 1]  # Nächster Punkt
            s = s + l1.distanz(l2)  # Addiere die Distanz zwischen den benachbarten Punkten zur Summe hinzu
        return s  # Gib die Gesamtsumme der Seitenlängen zurück

    def __str__(self):  # Methode zur Darstellung des Polygons als Zeichenkette
        s = f"Polygon: "  # Initialisiere die Zeichenkette mit "Polygon: "
        for punkt in self.pl:  # Iteriere über die Punkte des Polygons
            s = s + f"{punkt}"  # Füge jeden Punkt zur Zeichenkette hinzu
        return s  # Gib die Zeichenkette zurück

# Erstelle einige Punkte für die Verwendung in den Tests
P1 = Punkt(1, 1)
P2 = Punkt(3, 0)
P3 = Punkt(4, 1)
P4 = Punkt(2, 2)

# Teste die Klasse "Kreis"
M = Punkt(2, 3)
k1 = Kreis(M, 10)
print(k1)  # Gib den Kreis als Zeichenkette aus
print(k1.flaeche())  # Gib die Fläche des Kreises aus
print(k1.umfang())  # Gib den Umfang des Kreises aus

# Teste die Klasse "Dreieck"
t = Dreieck(P1, P2, P3)
print(t.umfang())  # Gib den Umfang des Dreiecks aus
print(t)  # Gib das Dreieck als Zeichenkette aus

# Teste die Klasse "Rechteck"
r = Rechteck(P1, P4)
print(r)  # Gib das Rechteck als Zeichenkette aus
print(r.umfang())  # Gib den Umfang des Rechtecks aus

# Teste die Klasse "Polygon"
polygonliste = [Punkt(1, 1), Punkt(2, 4), Punkt(3, 3.4), Punkt(4, 1)]  # Erstellen einer Liste von Punkten für das Polygon
p1 = Polygon(polygonliste)  # Erstellen einer Instanz der Klasse Polygon mit der Liste von Punkten
print(p1)  # Ausgabe der lesbaren Darstellung des Polygons
print(p1.umfang())  # Berechnen und Ausgabe des Umfangs des Polygons