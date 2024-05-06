import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
import os

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)
        p.loadSDF("world.sdf")