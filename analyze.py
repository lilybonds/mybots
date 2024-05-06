import numpy
import matplotlib.pyplot

bestPerGen=numpy.load("data/bestPerGenA.npy")
print(bestPerGen)
matplotlib.pyplot.plot(bestPerGen, label="Best", linewidth=2)
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Best fitness")
matplotlib.pyplot.show()


# backLegtargetAngles=numpy.load("data/backLegtargetAngles.npy")
# frontLegtargetAngles=numpy.load("data/frontLegtargetAngles.npy")
# matplotlib.pyplot.plot(backLegtargetAngles, label="Back Leg")
# matplotlib.pyplot.plot(frontLegtargetAngles, label="Front Leg")
# matplotlib.pyplot.legend()
# matplotlib.pyplot.show()