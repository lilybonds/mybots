import pybullet as p

class WORLD:
    def __intit__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")