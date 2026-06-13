import matplotlib.pyplot as plt

print("=== Ohm's Law Visualizer ===")

V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ω): "))

I = V / R

print(f"\nCurrent (I) = {I} A")

# Generate values for graph
voltages = list(range(0, int(V) + 1))
currents = [v / R for v in voltages]

plt.plot(voltages, currents, marker='o')
plt.title("Ohm's Law: V vs I")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (I)")
plt.grid(True)

plt.show()