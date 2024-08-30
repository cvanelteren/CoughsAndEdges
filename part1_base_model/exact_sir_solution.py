import matplotlib.pyplot as plt, numpy as np
from scipy.integrate import solve_ivp

# Numpy is the wirkhorse of the scientific computing in python
# It has functions for linear algebra, fourier transform, and random number capabilities
def step(t, x: np.ndarray,
         beta: float,
         gamma: float,
    ) -> np.ndarray:
    # note: beta encodes here a rate of encouter and a infection probability
    # Compute the instantaneous rate of change of the system
    # t is not used as our system is not "time" sensitive
    s, i, r = x # unpack the values
    ds = -beta * s * i / (s + i + r) # normalize to make the encouter rate into a probbility
    di = beta * s * i / (s + i + r) - gamma * i
    dr = gamma * i
    return np.asarray([ds, di, dr])


if __name__ == "__main__":
    beta  = 0.1
    gamma = 0.1
    # see scipy documentaiton for details on what solver
    # the solve_ivp function uses
    res = solve_ivp(
        step,  # update function
        t_span = (0, 100), # time span
        y0 = np.array([100, 1, 0]),  # initial conditions
        args = (beta, gamma) # additional arguments passed to your change function
    )
    # plot the results
    fig, ax = plt.subplots()
    ax.plot(res.y.T) # vectorized pass. Res.y is a matrix with the rows being the different states, we map the rows by transposing the matrix and matplotlib "knows" to plot each column as a different line
    plt.show(block = 1)
