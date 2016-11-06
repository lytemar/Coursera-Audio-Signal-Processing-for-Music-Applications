import matplotlib.pyplot as plt
import numpy as np
# import test_sinusoids
import A6Part3

from loadTestCases import load

testCase = load(3, 2)
print testCase['input']
print testCase['output']

result = A6Part3.estimateInharmonicity(**testCase['input'])
print result
