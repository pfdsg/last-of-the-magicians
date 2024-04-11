# -*- coding: utf-8 -*-
"""cheatsheet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yWT6AQcq7FDdWpI6j49-G_7BSBKkODSk
"""

import numpy as np
import matplotlib as plt

def bisecc(f, a, b, N, P):
  if f(a)*f(b) >= 0:
      print("Método da bissecção falha.")
      return None
  a_n = a
  b_n = b
  for n in range(1,N+1):
      m_n = (a_n + b_n)/2
      f_m_n = f(m_n)
      if abs((a_n - b_n)) <= P:
        print('Iteração número:', n, 'x = ', (a_n + b_n)/2)
        x = (a_n + b_n)/2
        return print('Solução mais próxima: ', x)
      elif f(a_n)*f_m_n < 0:
          a_n = a_n
          b_n = m_n
          print('Iteração número:', n, 'x = ', (a_n + b_n)/2)
      elif f(b_n)*f_m_n < 0:
          a_n = m_n
          b_n = b_n
          print('Iteração número:', n, 'x = ', (a_n + b_n)/2)
      else:
          print("Método da bissecção falha.")
          return None

def newton(f, dif_f, x0, P, itera):
  xn = x0
  for n in range (0, itera):
    fxn = f(xn)
    if abs(fxn) <= P:
      return print('Iteração número:', n, 'x = ', xn)
    dif_fxn = dif_f(xn)
    if dif_f(xn) == 0:
      return print('Iteração número:', n, 'Derivada nula, sem solução')
    print('Iteração número:', n, 'x = ', xn)
    xn = xn - fxn/dif_fxn
#teste

p = lambda x: x**3 - x**2 - 1
dp = lambda x: 3*x**2 - 2*x

newton(p, dp, 1, 1e-3, 1000)

import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros
m = 2  # massa em kg
F0 = 5.0  # Força em N
omega_0 = 4.0  # Frequência natural em rad/s
omega = 4.1  # Frequência em rad/s
x0 = 0.1  # Posição inicial em m
v0 = 0.3  # Velocidade inicial em m/s

def x(t):
    k = m * omega_0 ** 2
    A = F0 / (m * (omega_0**2 - omega**2))
    B = (v0 - A * omega) / omega_0
    return A * np.cos(omega * t) + B * np.cos(omega_0 * t)

t_values = np.linspace(0, 10, 1000)

x_values = x(t_values)

plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label='x(t)')
plt.title('Gráfico de x(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np

# Dados fornecidos
restanteP = 0.043  # Porcentagem de Pu239 desintegrado após 15 anos
t = 15  # Tempo em anos

# Calcula a constante de desintegração k
k = -np.log(1 - (restanteP/100)) / t

# Calcula a meia-vida usando a fórmula T_half = ln(2) / k
half_life = np.log(2) / k

# Imprime a meia-vida do Pu239
print(f"A meia-vida do Pu239 é aproximadamente {half_life:.2f} anos.")