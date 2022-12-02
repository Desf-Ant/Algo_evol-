from Solution import Solution
from random import randint, random

class Dieu :

    def __init__ (self) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        self.score_min = 1
        self.best_solution = None
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
            self.liste_solutions.append( Solution() )

    def calcul_score (self) :
        for sol in self.liste_solutions :
            fit = self.fitness_function(sol)
            pen = self.penality_function(sol)

            sol.score = fit - pen

    def fitness_function (self, solution) :
        somme = 0
        for i in range(solution.nb_attribut) : 
            somme += solution.attributs[i]
        return somme 
    
    def penality_function(self, solution) :
        penality = 0
        for i in range(solution.nb_attribut) :
            if solution.attributs[i] <= Solution.max_attribut_borne[i]/3 :
                penality += i*2
        return penality

    def selectionAndCroisement(self) :
        for i in range(int(self.nb_solutions/2)):
            indexS1, indexS2 = self.selection()
            self.croisement(indexS1, indexS2)
            
        if len(self.liste_next_generation) != self.nb_solutions :
            print("Moins de solution dans la nouvelle génération")

        self.liste_solutions = self.liste_next_generation
        self.liste_next_generation = []

    def selection(self) :
        s1, s2 = randint(0,self.nb_solutions-1), randint(0,self.nb_solutions-1)
        return s1, s2
    
    def croisement(self,indexS1, indexS2) :
        pivot = randint(0, Solution.nb_attribut-1)
        print("Index S1 S2 len solution",indexS1, indexS2, len(self.liste_solutions))
        if len(self.liste_solutions) == 0 :
            print(self.best_solution)
        attributs_1 = self.liste_solutions[indexS1].attributs[:pivot] + self.liste_solutions[indexS2].attributs[pivot:]
        attributs_2 = self.liste_solutions[indexS2].attributs[:pivot] + self.liste_solutions[indexS1].attributs[pivot:]

        new_sol_1 = Solution()
        new_sol_2 = Solution()
        new_sol_1.setAttributs(attributs_1)
        new_sol_2.setAttributs(attributs_2)

        self.liste_next_generation.append(new_sol_1)
        self.liste_next_generation.append(new_sol_2)
    
    def mutation(self) :
        for i in range(len(self.liste_next_generation)) :
            for j in range(len(self.liste_next_generation[i].attributs)) :
                if random() <= Solution.odd_to_mutate[j] :
                    self.liste_next_generation[i].attributs[j] = randint(0,Solution.max_attribut_borne[j])
    
    def goToNextGeneration(self):
        self.liste_solutions = self.liste_next_generation
        self.liste_next_generation = []

    def anotherGeneration(self):
        scores = []
        for sol in self.liste_solutions: 
            scores.append(self.fitness_function(sol))
        return scores.index(min(scores)), min(scores)

  
if __name__ == "__main__" :
    d = Dieu()
    print("La meilleure solution est", d.best_solution)
    