from core.Region import *
from core.Graphe import *
from core.Evolve import *
from gui.MainWindow import *
import time

w = 800
h = 600
nb_villes = 100

# Le problème à résoudre
r = Region ( w, h, nb_villes )

# Le graphe
g = Graphe ( r, nb_villes )

start = time.time()
e = Evolve(g)

print("Le temps pris :", time.time()-start)

g.best_parcours = e.best_solution.attributs
print(e.best_solution.attributs)
print(e.best_score)

fenetre = MainWindow( r, g )
fenetre.loop()
