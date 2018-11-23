# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
k = np.array([
             [1, 2, 3, 4],
             [5, 6, 7, 8]
             ])
k += 10
print(k.reshape(2, 2, 2))
print(k.ravel())
print(k.flatten())
k.shape = (2, 1, 4)
print(k)
k.resize(1, 1, 8)
print(k)
