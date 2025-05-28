# Re-import necessary packages after kernel reset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import os

# Define the system again
def system(t, y, a, b, K, V1, V2, V3, V4, K1, K2, K3, K4):
    P, Q, R = y
    dP = a * Q - b * P / (K + P)
    dQ = V1 * (1 - Q) / (K1 + (1 - Q)) - V2 * R * Q / (K2 + Q)
    dR = P * V3 * (1 - R) / (K3 + (1 - R)) - V4 * R / (K4 + R)
    return [dP, dQ, dR]

# Parameters and initial condition
params = (0.1, 0.1, 0.2, 1.0, 1.5, 6.0, 2.5, 0.01, 0.01, 0.01, 0.01)
y0 = [0.5, 0.2, 0.9]
t_span = (0, 20)
t_eval = np.linspace(*t_span, 400)

# Solve system
sol = solve_ivp(lambda t, y: system(t, y, *params), t_span, y0, t_eval=t_eval, rtol=1e-6, atol=1e-9)
P, Q, R, t = sol.y[0], sol.y[1], sol.y[2], sol.t

# Setup figure: left for schematic dots, right for plot
fig = plt.figure(figsize=(9, 6))  # total figure size
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 3])  # 1 row, 2 cols

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax1.set_xlim(-1, 3) #(-0.2, 1.2)
ax1.set_ylim(0, 1.05) #(-1, 3)
ax1.axis('off')
for x in [0, 1, 2]:
    ax1.vlines(x, 0, 1, colors='gray', linestyles='dotted')

# Dots for P, Q, R
dot_P = plt.Circle((0, P[0]), 0.05, color='blue', zorder=5, clip_on=False)
dot_Q = plt.Circle((1, Q[0]), 0.05, color='green', zorder=5, clip_on=False)
dot_R = plt.Circle((2, R[0]), 0.05, color='red', zorder=5, clip_on=False)
ax1.add_patch(dot_P)
ax1.add_patch(dot_Q)
ax1.add_patch(dot_R)

# Plot axis
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1.05)
# line_P, = ax2.plot([], [], 'b-', label='P')
# line_Q, = ax2.plot([], [], 'g-', label='Q')
# line_R, = ax2.plot([], [], 'r-', label='R')
line_P, = ax2.plot(t, P, 'b-', label='P')
line_Q, = ax2.plot(t, Q, 'g-', label='Q')
line_R, = ax2.plot(t, R, 'r-', label='R')
ax2.legend()
ax2.set_xlabel("Time Period")
ax2.set_ylabel("Value")

# Animation update
def update(i):
    dot_P.center = (0, P[i])
    dot_Q.center = (1, Q[i])
    dot_R.center = (2, R[i])
    window = 20
    current_time = t[i]

    # FULL precomputed data from the beginning (not building over time)
    t_shifted = t[i] - t  # shift time: current point at x = 0
    mask = (t_shifted >= 0) & (t_shifted <= 20)

    line_P.set_data(t_shifted[mask], P[mask])
    line_Q.set_data(t_shifted[mask], Q[mask])
    line_R.set_data(t_shifted[mask], R[mask])

    ax2.set_xlim(0, 10)

    return dot_P, dot_Q, dot_R, line_P, line_Q, line_R

ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

# Save to gif
gif_path = "../plots/schematic_plus_plot_v_10.gif"
ani.save(gif_path, writer='pillow', fps=20)
plt.close()

gif_path