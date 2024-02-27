import pybullet as p
import pyrosim
import pybullet_data
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __intit__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.world=WORLD()
        self.robot=ROBOT()