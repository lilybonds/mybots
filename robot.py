import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.motors={}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
    
    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR (linkName)
    
    def Sense(self,t):
        for key,value in self.sensors.items():
            value.Get_Value(t)

    def Prepare_To_Act(self):
        pass
        # self.sensors={}
        # for linkName in pyrosim.linkNamesToIndices:
        # self.sensors[linkName] = SENSOR (linkName)
    
    def Act(self):
        for key,value in self.motors.items():
            value.Set_Value()
