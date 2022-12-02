from random import random
from core.Graphe import *
from core.Candidat import *

def __init__ (self) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        #self.run()
        self.graphe = Graphe()


def initialize(self):
        liste_base =[]
        for i in range(100):
            liste_base.append(i)
        for _ in range(self.nb_solutions) :
            self.liste_solutions.append(Candidat(shuffle(liste_base))  )


def calcul_score (self) :
        for sol in self.liste_solutions :
            fit = self.fitness_function(sol)
            pen = self.penality_function(sol)

            sol.score = fit + pen


def fitness_function (self, solution) :
        somme = 0
        for i in range(1,len(solution)) : 
            somme += self.graphe.matrice_distance[solution[i]][solution[i-1]]
        return somme 
    
def penality_function(self, solution) :
        penality = 0
        test = 0
        for i in range(len(solution)) : 
            for j in range(100):
                if solution[i] == j :
                    test += 1
        if test != 100:
            penality = 2000
        return penality



def selectionAndCroisement(self) :
        for i in range(self.nb_solutions/2):
            indexS1, indexS2 = self.selection()
            self.croisement(indexS1, indexS2)
            
        if len(self.liste_next_generation) != self.nb_solutions :
            print("Moins de solution dans la nouvelle génération")

        self.liste_solutions = self.liste_next_generation
        self.liste_next_generation = []








def selection(self) :
        s1, s2 = randint(0,self.nb_solution), randint(0,self.nb_solutions)
        return s1, s2


def croisement(self,indexS1, indexS2) :
        pivot = randint(0, 100)
        attributs_1 = self.liste_solutions[indexS1][:pivot] + self.liste_solutions[indexS2][pivot:]
        attributs_2 = self.liste_solutions[indexS2][:pivot] + self.liste_solutions[indexS1][pivot:]

        new_sol_1 = Candidat(attributs_1)
        new_sol_2 = Candidat(attributs_2)
        

        self.liste_next_generation.append(new_sol_1)
        self.liste_next_generation.append(new_sol_2)
