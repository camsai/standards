import numpy as np
from camsai.standards import get_length

def test_get_length():
    vec = np.array([3, 4])
    assert get_length(vec) == 5.0

