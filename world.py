import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")