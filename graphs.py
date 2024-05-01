import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from main import dynamic_programming, Greedy


df = pd.read_excel('dataset.xlsx')

# Initialize lists to store extracted information
inventory_items = []
pack_sizes = []
unit_prices = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'Size' is not NaN and not "-"
    if not pd.isna(row['Size']) and row['Size'] != "-":
        # Add the information to the lists
        inventory_items.append(row['Inventory Item'])
        pack_sizes.append((row['Size']))
        unit_prices.append((row['Price']))


capacities = [2000,5000,8000,11000,14000,14500]

# Lists to store runtimes for dynamic programming and greedy
dp_runtimes = []
greedy_runtimes = []
total_items=len(inventory_items)

# Measure runtime for each capacity
for total_cap in capacities:
    # Measure runtime for dynamic programming
    start_time = time.time()
    dynamic_programming(total_cap, pack_sizes, unit_prices, total_items, inventory_items)
    dp_runtime = time.time() - start_time
    dp_runtimes.append(dp_runtime)

    # Measure runtime for greedy
    start_time = time.time()
    Greedy(total_cap, pack_sizes, unit_prices, total_items, inventory_items)
    greedy_runtime = time.time() - start_time
    greedy_runtimes.append(greedy_runtime)

# Plotting the graph
plt.plot(capacities, dp_runtimes, label='Dynamic Programming', marker='o')
plt.plot(capacities, greedy_runtimes, label='Greedy', marker='o')
plt.xlabel('Total Capacity')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Comparison for Different Capacities')
plt.legend()
plt.grid(True)
plt.show()