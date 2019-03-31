"""
Author: Christian Camilo Urcuqui López
Date: 30 March 2019
"""

import random

def generate_parent(length, geneSet):
    genes=[]
    while len(genes) < length:
        sampleSize = min(length -  len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)

def mutate(parent, geneSet):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = generate_parent(targetLen, geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    if bestFitness >= optimalFitness:
        return bestParent
    while True:
        child = mutate(bestParent, geneSet)
        childFitness =  get_fitness(child)
        
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent =  child