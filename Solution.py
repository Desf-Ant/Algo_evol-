from random import randint

class Solution: 

    max_attribut_borne = [10,20,30,40,50]
    nb_attribut = len(max_attribut_borne)

    def __init__(self) :
        self.attributs = []
        score = -1000

        for i in range (Solution.nb_attributs) : 
            self.attributs.append(randint(0,Solution.max_attribut_borne[i]))

    def setAttributs(self, lst_attributs) :
        self.attributs = lst_attributs