from tkinter.filedialog import askopenfile as apri
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

# Script per calcolare la trasformata di Fourier di un segnale e applicare un filtro

T   = 1         # Periodo
fs  = 1000      # Frequenza di campionamento
N   = T * fs    # Numero di punti

f1  = 2.5         # Frequenza di rotazione
f2  = 5.3         # Frequenza di rotazione

xt  = np.linspace(0, T, N)  # Vettore dei timesteps
yt  = np.zeros((N))
yt[:int(N//5)]  = 1
# yt  = np.sin(2 * np.pi * f1 * xt) + 5 * np.sin(2 * np.pi * f2 * xt) 
noise = np.random.normal(0, 0.05, N)
yt += noise

yf  = scipy.fft.rfft(yt)
plt.subplot(3, 1, 1)
plt.plot(xt, yt)

plt.subplot(3, 1, 2)
plt.plot(np.abs(yf) / N)

yf[50:] = 0

Yt  = scipy.fft.irfft(yf)
plt.subplot(3, 1, 3)
plt.plot(xt, Yt)
plt.show()