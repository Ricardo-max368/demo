import numpy as np
# Constantes y datos del problema
q = 1.6e-19  # Carga del protón en Coulombs
E = 8e4  # Campo eléctrico en V/m
d = 0.5  # Desplazamiento en metros
m = 1.67e-27  # Masa del protón en kg

# Cálculo del cambio en la energía potencial y conversión a energía cinética
delta_U = q * E * d
K = (delta_U)

# Cálculo de la velocidad
v = np.sqrt(2 * K / m)
print(v)
