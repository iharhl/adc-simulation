import matplotlib.pyplot as plt
import adc
import sine_wave
from constants import *

def main():

    (time, amplitude) = sine_wave.create(T=TIME, max=3.2)
    analog = sine_wave.add_noise(amplitude, scale = 0.05)

    adc1 = adc.Adc(resolution=12, volt_max=6.2, sampling_fq=25e3)
    digital = adc1.digitize(amplitude)

    plt.plot(time, amplitude, label="Sine voltage")
    plt.plot(time, analog, label="Sine voltage w/ noise")
    plt.plot(time, digital, label="Digitized voltage")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()