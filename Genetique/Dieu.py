from Solution import Solution
from random import randint, random

class Dieu :

    def __init__ (self) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        self.score_min = 149
        self.best_solution = None
        self.current_generation = 0
        self.generation_max = 50_000
        self.run()

    def run(self) : 
        self.initialize()
        index_score, score = self.anotherGeneration()
        while score < self.score_min :
            self.current_generation += 1
            self.calcul_score()
            self.selectionAndCroisement()
            self.mutation()
            self.goToNextGeneration()

            index_score, score = self.anotherGeneration()

            if self.current_generation >= self.generation_max :
                break
            print(self.current_generation)

        self.best_solution = self.liste_solutions[index_score]


    def initialize(self):
        for _ in range(self.nb_solutions) :
            self.liste_solutions.append( Solution() )

    def calcul_score (self) :
        for sol in self.liste_solutions :
            fit = self.fitness_function(sol)
            pen = self.penality_function(sol)

            sol.score = fit - pen
        
        #Trier la liste des toutes les solutions dans l'ordre des meilleures
        self.liste_solutions.sort(key= lambda sol: sol.score, reverse=True)

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
        


    def selection(self) :
        # Random
        #s1, s2 = randint(0,self.nb_solutions-1), randint(0,self.nb_solutions-1)
        
        #selectionner parmi les meilleurs (minimum fenetre 5%)
        borne_superieure = max(int((1-self.current_generation/self.generation_max)*self.nb_solutions), int(self.nb_solutions*0.05))
        s1, s2 = randint(0,borne_superieure), randint(0,borne_superieure)
        return s1, s2
    
    def croisement(self,indexS1, indexS2) :
        pivot = randint(0, Solution.nb_attribut-1)
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
        self.liste_solutions = list(self.liste_next_generation)
        self.liste_next_generation = []

    def anotherGeneration(self):
        scores = []
        for sol in self.liste_solutions: 
            scores.append(self.fitness_function(sol))
        return scores.index(max(scores)), max(scores)

  
if __name__ == "__main__" :
    d = Dieu()
    print("La meilleure solution est", d.best_solution.attributs)
    