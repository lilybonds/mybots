import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

amplitude=numpy.pi/4
frequency=1
phaseOffset=0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(2000)
frontLegSensorValues = numpy.zeros(2000)
targetAngles=numpy.linspace(0,2*numpy.pi,1000)
for angle in targetAngles:
    targetAngles[angle]=(numpy.pi/4)*targetAngles[angle]
numpy.save("data/targetAngles.npy",targetAngles)
exit()
for i in range (1,1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_BackLeg",controlMode = p.POSITION_CONTROL,targetPosition = targetAngles[i],maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = "Torso_FrontLeg",controlMode = p.POSITION_CONTROL,targetPosition = targetAngles[i],maxForce = 50)
p.disconnect()
print(backLegSensorValues)
numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)