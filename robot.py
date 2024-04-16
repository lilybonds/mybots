import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self,solutionID):
        self.myID=solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain"+solutionID+".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain"+solutionID+".nndf")
    
    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR (linkName)
    
    def Sense(self,t):
        for key,value in self.sensors.items():
            value.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR (jointName)
    
    def Act(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = (self.nn.Get_Value_Of(neuronName))
                desiredAngle=desiredAngle*c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId,desiredAngle)
        print("")
                
    def Think(self):
        self.nn.Update()
        ##self.nn.Print()
    
    def Get_Fitness(self):
       basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
       basePosition = basePositionAndOrientation[0]
       xPosition = basePosition[0]
       f=open("tmp"+str(self.myID)+".txt","w")
       f.write(str(xPosition))
       f.close()
       os.rename("tmp"+str(self.myID)+".txt" , "fitness"+str(self.myID)+".txt")
       
