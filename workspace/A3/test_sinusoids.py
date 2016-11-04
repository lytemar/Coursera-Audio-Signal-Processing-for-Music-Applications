import numpy as np
import sys

def sine_signal(fs, f1, f2):
	N = 2000
	A0 = 1
	x1 = np.zeros(N)
	x2 = np.zeros_like(x1)
	x = np.zeros_like(x1)
	x1 = A0 * np.cos(2 * np.pi * f1 * np.arange(N) / fs)
	x2 = A0 * np.cos(2 * np.pi * f2 * np.arange(N) / fs)
	x = x1 + x2
	return x
