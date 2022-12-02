import Solution
from random import randint

class Dieu :

    def __init__ (self) :
        self.liste_solutions = []
        self.liste_next_generation = []
        self.nb_solutions = 100
        self.run()

    def run(self) : 
        self.initialize()
        self.calcul_score()
        self.selectionAndCroisement()
        self.mutation()


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
        for i in range(solution.nb_attributs) : 
            somme += solution.attributs[i]
        return somme 
    
    def penality_function(self, solution) :
        penality = 0
        for i in range(solution.nb_attributs) :
            if solution.attributs[i] <= Solution.max_attribut_borne/3 :
                penality += i*2
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
        pivot = randint(0, Solution.nb_attribut-1)
        attributs_1 = self.liste_solutions[indexS1][:pivot] + self.liste_solutions[indexS2][pivot:]
        attributs_2 = self.liste_solutions[indexS2][:pivot] + self.liste_solutions[indexS1][pivot:]

        new_sol_1 = Solution()
        new_sol_2 = Solution()
        new_sol_1.setAttributs(attributs_1)
        new_sol_2.setAttributs(attributs_2)

        self.liste_next_generation.append(new_sol_1)
        self.liste_next_generation.append(new_sol_2)
    
    def mutation(self) :
        pass



if __name__ == "__main__" :
    d = Dieu()
    