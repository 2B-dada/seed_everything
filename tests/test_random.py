import random
from seed_everything import seed_everything

def test_random():
    sequance_1, sequance_2 = [], []
    
    seed_everything(10086)
    for i in range(10):
        sequance_1.append(random.random())

    seed_everything(10086)
    for i in range(10):
        sequance_2.append(random.random())

    assert sequance_1 == sequance_2, "Difference found, random behavior exist."