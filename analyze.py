import numpy
import matplotlib.pyplot

backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
print(backLegSensorValues)
print(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=2)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

backLegtargetAngles=numpy.load("data/backLegtargetAngles.npy")
frontLegtargetAngles=numpy.load("data/frontLegtargetAngles.npy")
matplotlib.pyplot.plot(backLegtargetAngles, label="Back Leg")
matplotlib.pyplot.plot(frontLegtargetAngles, label="Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()