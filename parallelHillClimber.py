from solution import SOLUTION
import constants as c
import copy
import os
import numpy
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents={}
        self.bestInGeneration=numpy.empty(c.numberOfGenerations)
        self.nextAvailableID=0
        for i in range(c.populationSize):
            self.parents[i]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID=self.nextAvailableID+1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.FindBest()

    def Spawn(self):
        self.children={}
        for key in self.parents:
            self.children[key]=copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID=self.nextAvailableID+1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()
        
    def Select(self):
        for key in self.parents:
            if(self.parents[key].fitness<self.children[key].fitness):
                self.parents[key]=self.children[key]
        
    def FindBest(self):
        bestFitness=-1
        for key in self.parents:
            if self.parents[key].fitness>bestFitness:
                bestFitness=self.parents[key].fitness
        self.bestInGeneration=numpy.append(self.bestInGeneration,bestFitness)
    
    def Print(self):
        print("")
        for key in self.parents:
            print("Parent Fitness: "+str(self.parents[key].fitness)+"; Child Fitness: "+str(self.children[key].fitness))
        print("")

    def Show_Best(self):
        print(self.bestInGeneration)
        numpy.save("data/bestPerGenA.npy",self.bestInGeneration)
        bestFitness=-1
        for key in self.parents:
            if self.parents[key].fitness>bestFitness:
                bestFitness=self.parents[key].fitness
                best=self.parents[key]
        best.Start_Simulation("GUI")
                

    def Evaluate(self,solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()