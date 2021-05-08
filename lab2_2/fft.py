import math
import sys
sys.path.append('../')
from lab2_1.dft import fourierCoefficient

def fastFourierTransformRecursion(signal):
  N = len(signal)
  if N == 1: return signal
  length = int(N / 2)
  spectre = [None] * N
  evens = fastFourierTransformRecursion(signal[::2])
  odds = fastFourierTransformRecursion(signal[1::2])
  for p in range(length):
    w = fourierCoefficient(p, N)
    product = odds[p] * w
    spectre[p] = evens[p] + product
    spectre[p + length] = evens[p] - product
  return spectre
