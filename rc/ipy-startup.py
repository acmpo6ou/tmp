import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def input_matrix(data_type=float):
    n, m = map(int, input().split())  # taking number of rows and column
    return np.array([input().strip().split() for _ in range(n)], data_type)
