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
            self.robot.Act()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = backLegtargetAngles[i],maxForce = c.max_force)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = frontLegtargetAngles[i],maxForce = c.max_force)

    def __del__(self):
        p.disconnect()