import random
import time as t
import matplotlib.pyplot as plt
import numpy as np

def gen_signal(n, W_max, N):
    signals = np.zeros(N)
    step = W_max/n
    for i in range(n):
        A = random.random()
        fi = random.random()
        w = i * step
    for t in range(N):
        signals[t] += A * np.sin(w * t + fi)
    return signals

def gen_time(n, W_max, N):
    time = []
    Dx = []
    Mx = []
    for i in range(N):
        start_time = t.time()
        data = gen_signal(n, W_max, i)
        end_time = t.time()
        Mx.append(math_expectation(data))
        Dx.append(dispersion(data))
        time.append(end_time - start_time)
    return [time, Mx, Dx]

def math_expectation(data):
    return np.mean(data)

def dispersion(data):
    return np.var(data)

def crosscorrelation(data1, data2):
    result = np.correlate(data1, data2, mode='same')
    return result

def autocorrelation(data):
    result = np.correlate(data, data, mode='full')
    return result[result.size // 2:]


n = int(input("Numbers of garmonics = "))
W_max = int(input("Border frequency = "))
N = int(input("Number of points = "))
I = int(input("Iterations(for time) = "))
signal1 = gen_signal(n, W_max, N)
signal2 = gen_signal(n, W_max, N)
data = gen_time(n, W_max, I)
plt.figure(1)
plt.plot(signal1)
plt.title('Random signals graph')
plt.figure(2)
plt.plot(data[0])
plt.title('Dependence of time graph')
plt.figure(3)
plt.plot(crosscorrelation(signal1, signal2))
plt.title('Crosscorrelation graph')
plt.figure(4)
plt.plot(autocorrelation(signal1))
plt.title('Autocorrelation graph')
plt.figure(5)
plt.plot(data[1], data[2])
plt.title('Mx from Dx')
plt.show()
print("Mathematical expectation = " + str(math_expectation(signal1)))
print("Dispersion = " + str(dispersion(signal1)))
