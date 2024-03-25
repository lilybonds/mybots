import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:
    def __init__(self,directOrGUI):
        self.directOrGUI=directOrGUI
        if directOrGUI=="DIRECT":
            physicsClient = p.connect(p.DIRECT)
        else:
            physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world=WORLD()
        self.robot=ROBOT()

    def Run(self):
        for t in range (c.loop_length):
            if self.directOrGUI=="GUI":
                time.sleep(c.sleep)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()