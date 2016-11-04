import matplotlib.pyplot as plt
import numpy as np
# import test_sinusoids
import A3Part1, A3Part2, A3Part3, A3Part4

from loadTestCases import load

#fs = 1000
#f = 100
#A0 = 10
#M = 25

testCase = load(4,1)

#(y, yfilt) = A3Part4.suppressFreqDFTmodel(x, fs, N)
(y, yfilt) = A3Part4.suppressFreqDFTmodel(**testCase['input'])

#x = A0 * np.cos(2 * np.pi * f * np.arange(M) / fs)
#x = np.array([1, 2, 3, 4, 1, 2, 3])
#(isRealEven, dftbuffer, X) = A3Part3.testRealEven(x)

#print (isRealEven, dftbuffer, X)

#plt.plot(mX)
#plt.show()
