from random_signals import signal_generator
from FFT import fft
import matplotlib.pyplot as plotter
from DFT import discrete_fourier_transform
from time import time

n = 14
w = 2000
N = 256


signal = signal_generator(n, w, N)

start1 = time()
spectre = abs(fft(signal))
end1 = time()
start2 = time()
dftsig = abs(discrete_fourier_transform(signal))
end2 = time()

fft_time = start1 - end1
dft_time = start2 - end2

print('FFT: {}'.format(fft_time))
print('DFT: {}'.format(dft_time))
# figure, axis = plotter.subplots(2, 1)

# plotter.subplots_adjust(left=0.1, top=0.9, bottom=0.1, right=0.99, hspace=0.5)

# axis[0].plot(range(N), signal)
# axis[0].set_title("Сигнал")
# axis[0].set(xlabel='Час', ylabel='Згенерований сигнал')

# axis[1].plot(range(N), spectre)
# axis[1].set_title("Швидке перетворення Фур'є")
# axis[1].set(xlabel='p', ylabel='F(p)')
# plotter.show()

plotter.stem([a - b for a, b in zip(spectre, dftsig)])
plotter.show()
