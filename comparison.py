import timeit
import matplotlib.pyplot as plt
import random
from main import dynamic_programming, Greedy, bruteforce

n_values = range(1, 2000)  #range of n

# Measure execution time for each value of n
times_dp = []
times_greedy = []
times_bruteforce = []
for n in n_values:
    items=[]
    p = [random.randint(10, 100) for _ in range(n)] 
    w = [random.randint(1, 20) for _ in range(n)] 
    for k in range(0,n):
        items.append(k)
    total_cap = (sum(w))/2 + 10
    # Measure time for cut_rod_memoized
    time_dp = timeit.timeit(lambda: dynamic_programming(total_cap, w, p, n,items), number=1)
    times_dp.append(time_dp)
    
    # Measure time for cut_rod_bottom_up
    time_Greedy = timeit.timeit(lambda: Greedy(total_cap, w, p, n,items), number=1)
    times_greedy.append(time_Greedy)

    # time_bruteforce = timeit.timeit(lambda: bruteforce(total_cap, w, p,items,n), number=1)
    # times_bruteforce.append(time_bruteforce)

plt.plot(n_values, times_dp, label='Dynammic Programming')
plt.plot(n_values, times_greedy, label='Greedy')
# plt.plot(n_values, times_bruteforce, label='Brute Force')
plt.xlabel(f'n = {n_values[-1]}')
plt.ylabel('Running Time (seconds)')
plt.title('Comparison Between the apporaches')
plt.legend()
plt.show()