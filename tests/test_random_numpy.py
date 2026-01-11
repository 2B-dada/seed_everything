import random
import numpy
from seed_everything import seed_everything

def test_random_numpy():
    seed_everything(10086)
    sequance_1 = numpy.random.rand(10)

    seed_everything(10086)
    sequance_2 = numpy.random.rand(10)

    assert numpy.allclose(sequance_1, sequance_2), "Difference found, random behavior exist."