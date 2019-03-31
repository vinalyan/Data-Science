import random
import unittest
import datetime
import genetic 


def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
        if expected == actual)    

def display(genes, target, startTime):
        timeDiff = datetime.datetime.now() - startTime
        fitness = get_fitness(genes, target)
        print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))

class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
    
    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)
        
    def guess_password(self, target):        
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(genes):
            display(genes, target, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best, target)

    


if __name__ == '__main__':
    unittest.main()