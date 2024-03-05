import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

class MOTOR:
    def __init__(self,jointName):
        self.jointName=jointName

    def Set_Value(self,robotId,desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = self.jointName,controlMode = p.POSITION_CONTROL,targetPosition = desiredAngle,maxForce = c.max_force)