import numpy as np
import matplotlib.pyplot as plt

# Zakres wartości x
x_values = np.linspace(0.01, 2, 400)

# Funkcje
def func1(x):
    return -np.log(x)

def func2(x):
    return -np.log(1 - x)

# Wykres
plt.figure(figsize=(10, 6))

# Pierwsza funkcja
plt.plot(x_values, func1(x_values), label=r'$-\log(f(x))$', color='blue')

# Druga funkcja
plt.plot(x_values, func2(x_values), label=r'$-\log(1 - f(x))$', color='red')

# Linie wskazujące miejsca x=0 i x=1
plt.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(x=1, color='black', linestyle='--', linewidth=0.8)

# Opisy osi
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function plot of $-\log(f(x))$ i $-\log(1 - f(x))$')
plt.legend()
plt.grid(True)
plt.ylim(-2, 5)  # Ustawienie zakresu osi Y dla lepszej czytelności
plt.show()
