import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

frontLegamplitude=numpy.pi/4
frontLegfrequency=10
frontLegphaseOffset=3*numpy.pi/4
backLegamplitude=numpy.pi/4
backLegfrequency=10
backLegphaseOffset=0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
xVals=numpy.linspace(0,2*numpy.pi,1000)
# targetAngles=numpy.pi/4*numpy.sin(xVals)
frontLegtargetAngles=frontLegamplitude * numpy.sin(frontLegfrequency * xVals + frontLegphaseOffset)
backLegtargetAngles=backLegamplitude * numpy.sin(backLegfrequency * xVals + backLegphaseOffset)
numpy.save("data/frontLegtargetAngles.npy",frontLegtargetAngles)
numpy.save("data/backLegtargetAngles.npy",backLegtargetAngles)
# exit()
for i in range (1,1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = backLegtargetAngles[i],maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = frontLegtargetAngles[i],maxForce = 50)

p.disconnect()
print(backLegSensorValues)
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)