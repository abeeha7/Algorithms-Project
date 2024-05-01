import random
from main import dynamic_programming, Greedy, bruteforce

n= 800
items=[]
p = [random.randint(10, 100) for _ in range(n)] 
w = [random.randint(1, 20) for _ in range(n)] 
for k in range(0,n):
    items.append(k)
total_cap = (sum(w))/2 + 10
max_value,items_dp= dynamic_programming(total_cap, w, p, n,items)
print("Maximum value by Dynamic Programming:", max_value)
print("Total items selected: ",len(items))

max_value1,items1= Greedy(total_cap, w, p, n,items)
print("Maximum value by Greedy:", max_value1)
print("Total items selected: ",len(items1))

