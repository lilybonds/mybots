import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
class ROBOT:
    def __intit__(self):
        self.sensors={}
        self.motors={}
        self.robotId = p.loadURDF("body.urdf")
