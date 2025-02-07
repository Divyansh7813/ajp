import numpy as np
import matplotlib.pyplot as plt

Square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
Housing_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])


plt.figure(figsize=(8, 6))
plt.scatter(Square_footage, Housing_prices, color='green', label='Data Points')
plt.title('Scatter Plot: House Size vs Selling Price')
plt.xlabel('Square Footage (sq. ft.)')
plt.ylabel('Selling Price ($000s)')
plt.grid(True)
plt.legend()
plt.show()