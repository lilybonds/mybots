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
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName=="Torso_BackLeg":
            self.amplitude=c.amplitude
            self.frequency=c.frequency/2
            self.phaseOffset=c.phaseOffset
        else:
            self.amplitude=c.amplitude
            self.frequency=c.frequency
            self.phaseOffset=c.phaseOffset
        self.xVals=numpy.linspace(0,2*numpy.pi,c.loop_length)
        self.motorValues=self.amplitude * numpy.sin(self.frequency * self.xVals + self.phaseOffset)

    def Set_Value(self,robotId,t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = self.jointName,controlMode = p.POSITION_CONTROL,targetPosition = self.motorValues[t],maxForce = c.max_force)

    def Save_Values(self):
        numpy.save("data/motorValues.npy",self.motorValues)