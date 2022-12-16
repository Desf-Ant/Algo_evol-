from random import random, shuffle
from core.Graphe import *
from core.Candidat import *

class Evolve :

    def __init__ (self,graphe) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        self.graphe = graphe
        self.score_min = 1
        self.best_solution = None
        self.liste_base =[]
        for i in range(100):
            self.liste_base.append(i)
        self.run()
        


    def run(self) : 
        self.initialize()
        index_score, score = self.anotherGeneration()
        while score > self.score_min :
            self.calcul_score()
            self.selectionAndCroisement()
            self.mutation()
            self.goToNextGeneration()
        print(self.liste_solutions)
        self.best_solution = self.liste_solutions[index_score]

    def initialize(self):
        

       
        for _ in range(self.nb_solutions) :
            shuffle(self.liste_base)
            self.liste_solutions.append(Candidat(self.liste_base)  )


    def calcul_score (self) :
        for sol in self.liste_solutions :
            fit = self.fitness_function(sol)
            pen = self.penality_function(sol)

            sol.score = fit + pen


    def fitness_function (self, solution) :
        somme = 0
        for i in range(1,len(solution.attributs)) : 
            #print(solution.attributs[i])
            somme += self.graphe.matrice_distances[solution.attributs[i]][solution.attributs[i-1]]
        return somme 
    
    def penality_function(self, solution) :
        penality = 0
        test = 0
        for i in range(len(solution.attributs)) : 
            for j in range(100):
                if solution.attributs[i] == j :
                    test += 1
        if test != 100:
            penality = 2000
        return penality



    def selectionAndCroisement(self) :
        for i in range(int(self.nb_solutions/2)):
            indexS1, indexS2 = self.selection()
            self.croisement(indexS1, indexS2)
            
        if len(self.liste_next_generation) != self.nb_solutions :
            print("Moins de solution dans la nouvelle génération")

        








    def selection(self) :
        s1, s2 = randint(0,self.nb_solutions-1), randint(0,self.nb_solutions-1)
        return s1, s2


    def croisement(self,indexS1, indexS2) :
        pivot = randint(1, 99)
        attributs_1 = self.liste_solutions[indexS1].attributs[:pivot] + self.liste_solutions[indexS2].attributs[pivot:]
        attributs_2 = self.liste_solutions[indexS2].attributs[:pivot] + self.liste_solutions[indexS1].attributs[pivot:]

        new_sol_1 = Candidat(attributs_1)
        new_sol_2 = Candidat(attributs_2)
        

        self.liste_next_generation.append(new_sol_1)
        self.liste_next_generation.append(new_sol_2)


    def mutation(self) :
        for i in range(len(self.liste_next_generation)) :
            for j in range(len(self.liste_next_generation[i].attributs)) :
                if random() <= Candidat.odd_to_mutate[j] :
                    self.liste_next_generation[i].attributs[j] = randint(0,99)
    
    def goToNextGeneration(self):
        self.liste_solutions = self.liste_next_generation
        self.liste_next_generation = []

    def anotherGeneration(self):
        scores = []
        for sol in self.liste_solutions: 
            scores.append(self.fitness_function(sol))
        return scores.index(min(scores)), min(scores)


if __name__ == "__main__" :
    d = Evolve()
    print("La meilleure solution est", d.best_solution)