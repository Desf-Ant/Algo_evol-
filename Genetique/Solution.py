from random import randint

class Solution: 

    max_attribut_borne = [10,20,30,40,50]
    odd_to_mutate = [0.1, 0.4, 0.6, 0.3, 0.2]
    nb_attribut = len(max_attribut_borne)

    def __init__(self) :
        self.attributs = []
        score = -1000

        for i in range (Solution.nb_attribut) : 
            self.attributs.append(randint(0,Solution.max_attribut_borne[i]))

    def setAttributs(self, lst_attributs) :
        self.attributs = lst_attributs