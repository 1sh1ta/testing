import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2025, 2027, 2030, 2033, 2040]
energy_kwh = [5254, 5050, 4320, 2620, 1420]
co2_kg = [10591, 9990, 3870, 3232, 2580]

# Plot Energy Consumption
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(years, energy_kwh, marker='o', color='green', linestyle='-')
plt.title('Household Energy Consumption Reduction (kWh/month)')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (kWh/month)')
plt.grid(True)

# Plot CO2 Emissions
plt.subplot(1, 2, 2)
plt.plot(years, co2_kg, marker='o', color='red', linestyle='-')
plt.title('Household CO₂ Emissions Reduction (kg/month)')
plt.xlabel('Year')
plt.ylabel('CO₂ Emissions (kg/month)')
plt.grid(True)

plt.tight_layout()
plt.show()
