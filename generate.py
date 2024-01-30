import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")


for j in range(0,5):
    length=1
    width=1
    height=1
    for k in range (0,5):
        length=1
        width=1
        height=1
        for i in range (0,10):
            pyrosim.Send_Cube(name="Box", pos=[j,k,i+.5] , size=[length,width,height])
            length=length*.9
            width=width*.9
            height=height*.9
           
pyrosim.End()

