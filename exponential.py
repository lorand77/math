import matplotlib.pyplot as plt
import math

a = math.e

x_values = [x * 0.1 for x in range(0, 61)]
y_values = [a**(-x) for x in x_values]

# Print the results
for x, y in zip(x_values, y_values):
    print(f"a^{x} = {y}")

# Plot the results
plt.plot(x_values, y_values, marker='o')
plt.grid(True)
plt.show()
