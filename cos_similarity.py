import numpy as np
import math


v1 = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
v2 = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
v3 = np.array([0.1, 0.3, 0.4, 0.2, 1, 0.1])


def magnitude(vector):
    mg = 0
    for number in vector:
        mg += number**2
    return math.sqrt(abs(mg))


def cos_similarity(vector1, vector2):
    denominator = magnitude(vector1) * magnitude(vector2)
    numerator = np.sum(abs(vector1) * abs(vector2))
    return 1 - math.acos((numerator/denominator))


print(cos_similarity(v1, v2))
