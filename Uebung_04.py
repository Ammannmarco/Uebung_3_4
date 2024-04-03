#Erstellen	Sie	eine	Applikation	mit	folgendem	GUI:
										
#Abbildung	1:	Screenshots	des	gefragten	GUI (Windows)
#a) Implementieren	Sie	das	GUI wie	abgebildet,	wählen	Sie	ein	geeignetes	Layout
#b) Ein	File-Menu	mit	den	Einträgen	Save	und	Quit	soll	hinzugefügt	werden
#c) wird	auf	den	Button	"Save"	gedrückt,	so	wird	ein	File	output.txt	angelegt,	welches	
#die	Daten	kommagetrennt	speichert,	also	für	oberes	Beispiel	wäre	der	Inhalt:
#Bernhard,Müller,6/25/1986,Gründenstrasse 40,4132,Muttenz,Schweiz
#d) Beim	Betätigen	des	"Quit"	Menus	wird	das	Programm	beendet
#e) Beim	Betätigen	des	"Save"	Menus	wird	der	Datensatz	wie	in	c)	gespeichert.
#Hinweis 1:	Die	QComboBox	(Auswahl	Land)	kann	folgendermassen	erstellt	werden:
#countries = QComboBox()
#countries.addItems(["Schweiz", "Deutschland", "Österreich"]


import sys  # Importiere das sys-Modul, das Funktionen und Variablen zum Interagieren mit dem Python-Interpreter bereitstellt
from PyQt5.QtCore import *  # Importiere alle Klassen und Funktionen aus dem PyQt5.QtCore-Modul
from PyQt5.QtWidgets import *  # Importiere alle Klassen und Funktionen aus dem PyQt5.QtWidgets-Modul

# Definiere eine benutzerdefinierte Klasse namens MyWindow, die von QMainWindow erbt
class MyWindow(QMainWindow):
    # Konstruktor der Klasse MyWindow
    def __init__(self):
        super().__init__()  # Rufe den Konstruktor der Elternklasse auf

        self.setWindowTitle("GUI - Programmierung")  # Setze den Fenstertitel

        # Layout erstellen (QFormLayout wird verwendet)
        layout = QFormLayout()

        # GUI-Elemente erstellen und initialisieren
        self.Vorname = QLineEdit()
        self.Name = QLineEdit()
        self.Geburtstag = QDateEdit()
        self.Adresse = QLineEdit()
        self.Postleizahl = QLineEdit()
        self.Ort = QLineEdit()
        self.Land = QComboBox()
        self.Button = QPushButton("Save")

        # Elemente zum ComboBox hinzufügen
        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"])

        # GUI-Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.Vorname)
        layout.addRow("Name:", self.Name)
        layout.addRow("Geburtstag:", self.Geburtstag)
        layout.addRow("Adresse:", self.Adresse)
        layout.addRow("Postleizahl:", self.Postleizahl)
        layout.addRow("Ort:", self.Ort)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.Button)

        # Menüleiste hinzufügen
        menubar = self.menuBar()
        file = menubar.addMenu("File")

        # Aktionen für das Menü erstellen
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        # Aktionen zum Menü hinzufügen
        file.addAction(self.save)
        file.addAction(self.quit)

        # Verknüpfungen für die Buttons festlegen
        self.Button.clicked.connect(self.textFile)
        self.save.triggered.connect(self.textFile)
        self.quit.triggered.connect(self.close)

        # Zentrale Widget erstellen und Layout setzen
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    # Methode zum Speichern der eingegebenen Daten in einer Textdatei
    def textFile(self):
        # Geburtsdatum im gewünschten Format extrahieren
        g = self.Geburtstag.date().toString("dd.MM.yyyy")
        # Daten zu einem Text zusammenstellen
        text = f"{self.Vorname.text()},{self.Name.text()},{g},{self.Adresse.text()},{self.Postleizahl.text()},{self.Ort.text()},{self.Land.currentText()}"
        # Text in eine Datei schreiben
        file = open("output.txt.", "w", encoding="utf-8")
        file.write(text)
        file.close()  # Datei schliessen
        print("Die Daten wurden erfolgreich gespeichert")

    # Methode zum Schliessen des Fensters
    def close(self):
        self.close()  # Schliesst das Fenster

# Hauptfunktion des Programms
def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()  # Instanz Fenster erstellen
    mainwindow.raise_()  # Fenster nach vorne bringen
    app.exec_()  # Applikations-Loop starten

# Überprüfen, ob das Skript direkt ausgeführt wird
if __name__ == '__main__':
    main()  # Hauptfunktion aufrufen