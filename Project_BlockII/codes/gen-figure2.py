import numpy as np
import matplotlib.pyplot as plt

import model_PQR as model
from steady_state import steady_state_Q, steady_state_R

# Define parameter value
a, b = 0.1, 0.1
V1, V2, V3, V4 = 1.0, 1.5, 6.0, 2.5
K, K1, K2, K3, K4 = 0.2, 0.01, 0.01, 0.01, 0.01
path_fig_2A = "plots/fig_2A.png" # Run from PROJECT_BLOCKII directory
path_fig_2B = "plots/fig_2B.png"

#Threshold calculation

P_star = model.compute_P_star(V3=V3, V4=V4, K3=K3, K4=K4)
R_star = model.compute_R_star(V1=V1, V2=V2, K1=K1, K2=K2)

print(f"P* ≈ {round(P_star, 3)}")
print(f"R* ≈ {round(R_star, 3)}")

# Array of P values
P_values = np.linspace(0, 1, 101)
# Compute R steady state values
R_values = [steady_state_R(P, V3, V4, K3, K4) for P in P_values]

# Array of R values
R_values_RQ = np.linspace(0, 1, 101)
# Compute Q steady state values
Q_values_RQ = [steady_state_Q(R, V1, V2, K1, K2) for R in R_values_RQ]

# Plot figure 2A
plt.figure(figsize=(5, 5))
plt.plot(P_values, R_values, color='#4169E1', marker='.', linestyle='', markersize=7, zorder=5, clip_on=False)
plt.axvline(P_star, color='#4169E1', linestyle='--', linewidth=1, label=f'$P^*$ ≈ {round(P_star, 3)}', alpha=0.7)
plt.xlabel("P", weight="bold", fontsize=14)
plt.ylabel("R", weight="bold", fontsize=14)
plt.title("R changes over P")
plt.minorticks_on()
plt.grid(which='major', color='gray', linewidth=0.8, alpha=0.5)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.1)
plt.legend(loc='center left')
plt.xlim(0,1)
plt.ylim(0,1)
plt.savefig(path_fig_2A, dpi=300, bbox_inches='tight')

# Plot
plt.figure(figsize=(5, 5))
plt.plot(R_values_RQ, Q_values_RQ, color='#DC143C', marker='.', linestyle='', markersize=7, zorder=5, clip_on=False)
plt.axvline(R_star, color='#DC143C', linestyle='--', linewidth=1, label=f'$R^*$ ≈ {round(R_star, 3)}', alpha=0.7)
plt.xlabel("R", weight="bold", fontsize=14)
plt.ylabel("Q", weight="bold", fontsize=14)
plt.title("Q changes over R")
plt.minorticks_on()
plt.grid(which='major', color='gray', linewidth=0.8, alpha=0.5)
plt.grid(which='minor', color='gray', linewidth=0.5, alpha=0.1)
plt.xlim(0,1)
plt.ylim(0,1)
plt.legend(loc='center left')
plt.savefig(path_fig_2B, dpi=300, bbox_inches='tight')

