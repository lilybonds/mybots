import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
class SENSOR:
    def __init__(self, linkName):
        self.linkName=linkName
        self.values = numpy.zeros(c.loop_length)

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t==c.loop_length-1:
            print(self.values)