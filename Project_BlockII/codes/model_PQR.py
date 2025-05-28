def dP_dt(t, P, Q, a, b, K):
    """Equation (1a): dP/dt"""
    return a * Q - b * P / (K + P)

def dQ_dt(t, Q, R, V1, V2, K1, K2):
    """Equation (1b): dQ/dt"""
    term1 = V1 * (1 - Q) / (K1 + (1 - Q))
    term2 = V2 * R * Q / (K2 + Q)
    return term1 - term2

def dR_dt(t, R, P, V3, V4, K3, K4):
    """Equation (1c): dR/dt"""
    term1 = P * V3 * (1 - R) / (K3 + (1 - R))
    term2 = V4 * R / (K4 + R)
    return term1 - term2

def compute_P_star(V3, V4, K3, K4):
    """
    Compute the threshold value P* from equation (2a)
    """
    return (V4 / V3) * ((1 + 2 * K3) / (1 + 2 * K4))

def compute_R_star(V1, V2, K1, K2):
    """
    Compute the threshold value R* from equation (2b)
    """
    return (V1 / V2) * ((1 + 2 * K2) / (1 + 2 * K1))