import numpy as np
from control import matlab 
import matplotlib.pyplot as plt
from sine_wave import add_noise

def rc_filter(R: int, C: float):

    ### Data
    # V(t) => input (source voltage)
    # V_c(t) => output (voltage across capacitor)
    # Gp(s) = V_c(s)/V(s) => tf
    #### Solution
    # V(t) = V_r(t) + V_c(t)
    # i(t) = i_c(t) = i_r(t)
    # i(t) = C * dV_c(t)/dt
    # i(t) = V_r(t) / R => V_r(t) = R * i(t) = R * C * dV_c(t)/dt
    # ==> V(t) = R * C * dV_c(t)/dt + V_c(t)
    # take laplace: V(s) = R * C * s * V_c(s) + V_c(s) = V_c(s) * (R * C * s + 1)
    # ==> Gp(s) = V_c(s) / V(s) = 1 / (R * C * s + 1)

    # transfer function
    P = matlab.tf([0, 1], [0, R*C, 1])

    # step response
    T = np.arange(0, 0.01, 0.00001)
    y, t = matlab.step(P, T)

    # forced responce
    Fq = 2e2
    max = 5
    U = (np.sin(2*np.pi*Fq*T)+1)*0.5*max
    U = add_noise(U)
    y, t, x0 = matlab.lsim(P, U, T)

    # plot
    plt.plot(t, y, label="V_capacitor")
    plt.plot(t, U, label="V_source")
    plt.legend()
    plt.show()
        
if __name__ == "__main__":
    """ Separate script to play around with RC filtering through use of transfer functions """
    rc_filter(4700, 49e-9)