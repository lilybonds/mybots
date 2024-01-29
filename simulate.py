import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range (1,1000):
    time.sleep(1/60)
    p.stepSimulation()
    print(x)
p.disconnect()
