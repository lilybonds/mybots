import numpy
import matplotlib.pyplot

# backLegSensorValues=numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues=numpy.load("data/frontLegSensorValues.npy")
# print(backLegSensorValues)
# print(frontLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=2)
# matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()

targetAngles=numpy.load("data/targetAngles.npy")
matplotlib.pyplot.plot(targetAngles, numpy.sin(targetAngles))
matplotlib.pyplot.show()