import numpy
import matplotlib.pyplot

bestPerGen=numpy.load("data/bestPerGenB.npy")
print(bestPerGen)
matplotlib.pyplot.plot(bestPerGen, label="Best", linewidth=2)
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Best fitness")
matplotlib.pyplot.show()