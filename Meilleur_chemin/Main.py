from core.Region import *
from core.Graphe import *
from gui.MainWindow import *

w = 800
h = 600
nb_villes = 100

# Le problème à résoudre
r = Region ( w, h, nb_villes )

# Le graphe
g = Graphe ( r, nb_villes )

fenetre = MainWindow( r, g )
fenetre.loop()
