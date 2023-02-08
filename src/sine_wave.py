import numpy as np
from constants import *

def create(F: int = 5e2, T: float = 2e-3, max: float = 1):

    # F -- No. of cycles per second [Hz]
    # T -- Time period [s]
    # N -- No. of samples during time T

    N: int = int(T * TIMESTEP)

    time: list[float] = np.linspace(0, T, N)
    amplitude: list[float] = (np.sin(2*np.pi*F*time)+1)*0.5*max

    return (time, amplitude)

def add_noise(signal: list[float], scale: float = 0.1):
    noise = np.random.normal(scale=scale, size=len(signal))
    noisy_signal = signal + noise
    return noisy_signal