import numpy
import matplotlib.pyplot

bestPerGenA1=numpy.load("data/bestPerGenA1.npy")
bestPerGenA2=numpy.load("data/bestPerGenA2.npy")
bestPerGenA3=numpy.load("data/bestPerGenA3.npy")

matplotlib.pyplot.plot(bestPerGenA1, label="Hexapod", linewidth=2, color='orange')
matplotlib.pyplot.plot(bestPerGenA2, linewidth=2, color='orange')
matplotlib.pyplot.plot(bestPerGenA3, linewidth=2, color='orange')

bestPerGenB1=numpy.load("C:/Users/lilyb/Documents/CS3060/mybots-1/data/bestPerGenB1.npy")
bestPerGenB2=numpy.load("C:/Users/lilyb/Documents/CS3060/mybots-1/data/bestPerGenB2.npy")
bestPerGenB3=numpy.load("C:/Users/lilyb/Documents/CS3060/mybots-1/data/bestPerGenB3.npy")

matplotlib.pyplot.plot(bestPerGenB1, label="Quadruped", linewidth=2, color='blue')
matplotlib.pyplot.plot(bestPerGenB2, linewidth=2, color='blue')
matplotlib.pyplot.plot(bestPerGenB3, linewidth=2, color='blue')

matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Best fitness")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


# backLegtargetAngles=numpy.load("data/backLegtargetAngles.npy")
# frontLegtargetAngles=numpy.load("data/frontLegtargetAngles.npy")
# matplotlib.pyplot.plot(backLegtargetAngles, label="Back Leg")
# matplotlib.pyplot.plot(frontLegtargetAngles, label="Front Leg")
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()