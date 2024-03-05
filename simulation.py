import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world=WORLD()
        self.robot=ROBOT()

    def Run(self):
        for t in range (1,c.loop_length):
            time.sleep(c.sleep)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            
    def __del__(self):
        p.disconnect()