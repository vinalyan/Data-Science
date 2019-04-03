"""
Author: Christian Camilo Urcuqui López
Date: 3 April 2019
"""


import unittest
import datetime
import genetic


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(''.join(candidate.Genes), candidate.Fitness, str(timeDiff)))

class OneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
        startTime = datetime.datetime.now()
        
        def fnDisplay(candidate):
            display(candidate, startTime)
            
        def fnGetFitness(genes):
            return get_fitness(genes)
        
        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length, optimalFitness, geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)
           
if __name == '__main__':
    unitest.main()
