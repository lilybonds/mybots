import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID=nextAvailableID
        self.weights=2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)-1
        self.weights=self.weights*2-1

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py "+directOrGUI+" "+str(self.myID))
    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName="fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile=open(fitnessFileName,"r")
        self.fitness=float(fitnessFile.read())
        fitnessFile.close()
        os.system("del fitness"+str(self.myID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[1,1,1])
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1.7,1,1])
        #left side
        pyrosim.Send_Joint( name = "Torso_BackLeftLeg" , parent= "Torso" , child = "BackLeftLeg" , 
                            type = "revolute", position = [-0.3,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[-0.3,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "BackLeftLeg_BackLeftLowerLeg" , parent= "BackLeftLeg" , child = "BackLeftLowerLeg" , 
                            type = "revolute", position = [-0.3,-1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Torso_MiddleLeftLeg" , parent= "Torso" , child = "MiddleLeftLeg" , 
                            type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "MiddleLeftLeg_MiddleLeftLowerLeg" , parent= "MiddleLeftLeg" , child = "MiddleLeftLowerLeg" , 
                            type = "revolute", position = [0,-1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="MiddleLeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , 
                            type = "revolute", position = [0.3,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[0.3,-0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "FrontLeftLeg_FrontLeftLowerLeg" , parent= "FrontLeftLeg" , child = "FrontLeftLowerLeg" , 
                            type = "revolute", position = [0.3,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        #right side
        pyrosim.Send_Joint( name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , 
                            type = "revolute", position = [-0.3,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[-0.3,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "BackRightLeg_BackRightLowerLeg" , parent= "BackRightLeg" , child = "BackRightLowerLeg" , 
                            type = "revolute", position = [-0.3,1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Torso_MiddleRightLeg" , parent= "Torso" , child = "MiddleRightLeg" , 
                            type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="MiddleRightLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "MiddleRightLeg_MiddleRightLowerLeg" , parent= "MiddleRightLeg" , child = "MiddleRightLowerLeg" , 
                            type = "revolute", position = [0,1,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="MiddleRightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Torso_FrontRightLeg" , parent= "Torso" , child = "FrontRightLeg" , 
                            type = "revolute", position = [0.3,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[0.3,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint( name = "FrontRightLeg_FrontRightLowerLeg" , parent= "FrontRightLeg" , child = "FrontRightLowerLeg" , 
                            type = "revolute", position = [0.3,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.End()
    
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "MiddleLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "BackRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "MiddleRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontRightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_BackLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeftLeg_BackLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "MiddleLeftLeg_MiddleLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "FrontLeftLeg_FrontLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackRightLeg_BackRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_MiddleRightLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "MiddleRightLeg_MiddleRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "FrontRightLeg_FrontRightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self):
        randomRow=numpy.random.randint(0,c.numSensorNeurons-1)
        randomColumn=numpy.random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn]=numpy.random.random()*2-1

    def Set_ID(self,nextAvailableID):
        self.myID=nextAvailableID