from scipy.integrate import solve_ivp
from model_PQR import dR_dt, dQ_dt

# Define the steady state R value for a given P
def steady_state_R(P, V3, V4, K3, K4, R0=0.01):

    # Solve for R using a large time to approach steady state
    sol = solve_ivp(dR_dt, [0, 50], [R0], args=(P, V3, V4, K3, K4), rtol=1e-6, atol=1e-9)
    return sol.y[0, -1]

# Define the steady state Q value for a given R
def steady_state_Q(R, V1, V2, K1, K2, Q0=0.01):

    # Solve for R using a large time to approach steady state
    sol = solve_ivp(dQ_dt, [0, 50], [Q0], args=(R, V1, V2, K1, K2), rtol=1e-6, atol=1e-9) # , t_eval=[50]
    return sol.y[0, -1] #sol.y[0][0]
