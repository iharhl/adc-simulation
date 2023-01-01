from constants import *

class Adc:
    def __init__(self, resolution: int, volt_max: float, sampling_fq: int):
        self.resolution: int = resolution # [bits]
        self.volt_max: float = volt_max # [V]
        self.sampling_fq: int = sampling_fq # samples/s [Hz]
        # voltage step size
        self.step: float = volt_max / resolution**2
        # simulate sampling fq over timestep
        self.skip_samples: int = int(TIMESTEP/self.sampling_fq - 1)

    def digitize(self, signal: list[float]) -> list[float]:
        dig_signal: list[float] = []
        count: int = self.skip_samples
        for i in signal:
            if count == self.skip_samples:
                count = 0
                step_diff = round((self.volt_max-i)/self.step)
                dig_signal.append(self.volt_max - (step_diff*self.step))
            else:
                count += 1
                dig_signal.append(self.volt_max - (step_diff*self.step))
        return dig_signal


