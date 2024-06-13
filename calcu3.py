import numpy as np
# Constantes y conversiones
k = 8.99e9  # Nm^2/C^2
q_pos = 7.00e-6  # C
q_neg = -7.00e-6  # C
r_pos = np.sqrt(17) * 0.01  # metros
r_neg = 0.01  # metros

# Cálculo del potencial eléctrico en el punto medio
V_pos = k * (q_pos / r_pos)
V_neg = k * (q_neg / r_neg)
V_total = V_pos + 2 * V_neg  # Sumando el potencial de las dos cargas negativas

print(V_total)
