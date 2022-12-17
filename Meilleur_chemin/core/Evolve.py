from random import random, shuffle
from core.Graphe import *
from core.Candidat import *

class Evolve :

    def __init__ (self,graphe) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        self.graphe = graphe
        self.score_min = 100_000
        self.best_solution = None
        self.liste_base =[]
        self.current_generation = 0
        self.generation_max = 5_000
        for i in range(100):
            self.liste_base.append(i)
        self.run()
        


    def run(self) : 
        self.initialize()
        index_score, score = self.anotherGeneration()
        while True:
            self.current_generation += 1
            self.calcul_score()
            self.selectionAndCroisement()
            self.mutation()
            self.goToNextGeneration()

            index_score, score = self.anotherGeneration()

            if self.current_generation >= self.generation_max :
                break
            if self.current_generation % 100 == 0 : 
                print(self.current_generation)

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
        if len(set(solution.attributs)) != len(solution.attributs) :
            penality = 500_000 * (len(solution.attributs) - len(set(solution.attributs)) )
            # print("manque", (len(solution.attributs) - len(set(solution.attributs)) ), "villes")
        if penality < 0 : print("bizarre", penality)
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

        allCities_1 = [i for i in range(100)]
        allCities_2 = [i for i in range(100)]
        index_ville_double_1 = []
        index_ville_double_2 = []

        ## On regarde toutes les villes non visitées + on recupère les index des doublons
        for i in range(len(attributs_1)) :
            if attributs_1[i] in allCities_1 :
                allCities_1[attributs_1[i]] = -1
            else  :
                index_ville_double_1.append(i)

        for i in range(len(attributs_2)) :
            if attributs_2[i] in allCities_2 :
                allCities_2[attributs_2[i]] = -1
            else  :
                index_ville_double_2.append(i)
        
        ## On supprime les -1 (villes deja visitées) -> reste toutes les villes non visitées
        allCities_1 = list(filter(lambda city: city != -1, allCities_1))
        allCities_2 = list(filter(lambda city: city != -1, allCities_2))

        ## On remplace les villes doublons avec celles non visitées
        for i in range(len(index_ville_double_1)) :
            attributs_1[index_ville_double_1[i]] = allCities_1[i]

        for i in range(len(index_ville_double_2)) :
            attributs_2[index_ville_double_2[i]] = allCities_2[i]

        new_sol_1 = Candidat(attributs_1)
        new_sol_2 = Candidat(attributs_2)
        

        self.liste_next_generation.append(new_sol_1)
        self.liste_next_generation.append(new_sol_2)


    def mutation(self) :
        for i in range(len(self.liste_next_generation)) :
            for j in range(len(self.liste_next_generation[i].attributs)) :
                if random() <= Candidat.odd_to_mutate[j] :
                    index = randint(0,99)
                    self.liste_next_generation[i].attributs[j], self.liste_next_generation[i].attributs[index] = self.liste_next_generation[i].attributs[index], self.liste_next_generation[i].attributs[j]
    
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