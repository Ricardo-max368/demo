import numpy as np

# Definimos eps0, k
eps0 = 8.85e-12
k = (1 / (4*np.pi*eps0))

# Definimos de microC to C
def microc_to_c(micro_coulombs):
    coulombs = micro_coulombs / 1000000
    return coulombs

# Calculando las distancias
r1 = 4  # metros
r2 = np.sqrt(25)  # metros

# Analisis completo
resultado = k* (microc_to_c(2)/r1 - microc_to_c(6)/r2)

# Potencial total
print(microc_to_c(5))
