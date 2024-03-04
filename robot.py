import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
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
        for key,value in self.motors.items():
            value.Set_Value(self.robotId,t)
