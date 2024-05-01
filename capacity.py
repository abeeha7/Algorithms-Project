import time
import matplotlib.pyplot as plt
import pandas as pd
from main import dynamic_programming, Greedy, bruteforce

df = pd.read_excel('dataset.xlsx')

# Initialize lists to store extracted information
inventory_items = []
pack_sizes = []
unit_prices = []

# Iterate over each row in the DataFrame, only consider the first 30 rows
for index, row in df.iterrows():
    # Check if 'Size' is not NaN and not "-"
    if not pd.isna(row['Size']) and row['Size'] != "-":
        # Add the information to the lists
        inventory_items.append(row['Inventory Item'])
        pack_sizes.append(row['Size'])
        unit_prices.append(row['Price'])


total_items = len(inventory_items)
#Total capacity for testing


# Initialize lists to store runtimes
dp_runtimes = []
greedy_runtimes = []
bruteforce_runtimes = []

# Loop from 1 to 30
for n in range(1, total_items):
    # Measure runtime for dynamic programming
    total_cap = (sum(pack_sizes[:n]))/2 + 10
    start_time = time.time()
    dynamic_programming(total_cap, pack_sizes[:n], unit_prices[:n], n, inventory_items[:n])
    dp_runtime = time.time() - start_time
    dp_runtimes.append(dp_runtime)

    # Measure runtime for greedy
    start_time = time.time()
    Greedy(total_cap, pack_sizes[:n], unit_prices[:n], n, inventory_items[:n])
    greedy_runtime = time.time() - start_time
    greedy_runtimes.append(greedy_runtime)

    # Measure runtime for brute force
    start_time = time.time()
    bruteforce(total_cap,pack_sizes[:n], unit_prices[:n],inventory_items[:n],n)
    bruteforce_runtime = time.time() - start_time
    bruteforce_runtimes.append(bruteforce_runtime)

# Plotting the graph with lines instead of markers
plt.plot(range(1, total_items), dp_runtimes, label='Dynamic Programming')
plt.plot(range(1, total_items), greedy_runtimes, label='Greedy')
# plt.plot(range(1, total_items), bruteforce_runtimes, label='Brute Force')
plt.xlabel('Number of Items (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime Comparison for Different Values of n')
plt.legend()
plt.grid(True)
plt.show()
