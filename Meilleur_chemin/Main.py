from core.Region import *
from core.Graphe import *
from core.Evolve import *
from gui.MainWindow import *

w = 800
h = 600
nb_villes = 100

# Le problème à résoudre
r = Region ( w, h, nb_villes )

# Le graphe
g = Graphe ( r, nb_villes )

t = Evolve(g)

t.best_solution
g.best_parcours = t.best_solution.attributs
print(t.best_solution.attributs)

fenetre = MainWindow( r, g )
fenetre.loop()
