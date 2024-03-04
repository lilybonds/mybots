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
        self.amplitude=c.frontLegamplitude
        self.frequency=c.frontLegfrequency
        self.phaseOffset=c.frontLegphaseOffset
        self.xVals=numpy.linspace(0,2*numpy.pi,c.loop_length)
        self.motorValues=self.amplitude * numpy.sin(self.frequency * self.xVals + self.phaseOffset)

    def Set_Value(self):
        pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = self.jointName,controlMode = p.POSITION_CONTROL,targetPosition = self.motorValues[t],maxForce = c.max_force)