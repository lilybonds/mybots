import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
from simulation import SIMULATION
from world import WORLD
from robot import ROBOT

simulation = SIMULATION()

# #robotId = p.loadURDF("body.urdf")
# backLegSensorValues = numpy.zeros(c.loop_length)
# frontLegSensorValues = numpy.zeros(c.loop_length)
# xVals=numpy.linspace(0,2*numpy.pi,c.loop_length)
# frontLegtargetAngles=c.frontLegamplitude * numpy.sin(c.frontLegfrequency * xVals + c.frontLegphaseOffset)
# backLegtargetAngles=c.backLegamplitude * numpy.sin(c.backLegfrequency * xVals + c.backLegphaseOffset)
# # numpy.save("data/frontLegtargetAngles.npy",frontLegtargetAngles)
# # numpy.save("data/backLegtargetAngles.npy",backLegtargetAngles)

# for i in range (1,c.loop_length):
#     time.sleep(c.sleep)
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = backLegtargetAngles[i],maxForce = c.max_force)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = simulation.robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = frontLegtargetAngles[i],maxForce = c.max_force)

# p.disconnect()
# # print(backLegSensorValues)
# # numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
# # numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)