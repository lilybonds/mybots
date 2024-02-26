import pybullet as p
import pyrosim
import pybullet_data

class SIMULATION:
    def __intit__(self):
        self.world=WORLD()
        self.robot=ROBOT()
        self.robotId = p.loadURDF("body.urdf")
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robotId)