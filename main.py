import pandas as pd
import numpy as np

def write_items_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            file.write(item + '\n')

def bruteforce(W, wt, val, items, n):

    if W == 0:
        return 0, []  # If no items left, return minimum profit 0 and empty list of selected items
    if W < 0 or n <= 0:
        return float('inf'), []  # If capacity is 0, minimum profit is 0 and no items selected
    
    # If the current item's weight is more than the remaining capacity,
    # then this item cannot be included in the knapsack
    if wt[n - 1] > W:
        return float('inf'), []  # Return infinity as minimum profit and no items selected
    
    # Recursive Case
    else:
        # Choose the minimum between including the current item
        # and excluding the current item
        include_profit, include_items = bruteforce(int(W-wt[n-1]), wt, val, items, n-1)
        include_profit += val[n - 1]  # Add current item's value to profit
        include_items = include_items + [items[n - 1]]  # Include current item in selected items
        
        exclude_profit, exclude_items = bruteforce(int(W), wt, val,items,n-1)
        
        # Return the minimum profit and selected items
        if include_profit < exclude_profit:
            return include_profit, include_items
        else:
            return exclude_profit, exclude_items
        

def dynamic_programming(cap, weight, profit, n, item):
    K = [[float('inf') for _ in range(int(cap) + 1)] for _ in range(n + 1)]
    #if capacity is 0, then profit is also 0 - base case
    for i in range(n+1):
        K[i][0]=0
    # Build table K[][] in bottom up manner
    for i in range(1,n + 1):
        for w in range(1,int(cap) + 1):
            if weight[i - 1] <= w:
                K[i][w] = min(profit[i - 1] + K[i - 1][int(w - weight[i - 1])], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Trace back the items chosen
    items_selected = []
    min_value = K[n][int(cap)]
    w = int(cap)
    for i in range(n, 0, -1):
        if min_value <= 0:
            break
        if min_value == K[i - 1][w]:
            continue
        else:
            items_selected.append(item[i - 1])
            min_value -= profit[i - 1]
            w -= int(weight[i - 1])
    return K[n][int(cap)], items_selected


def Greedy(cap, weight, profit, n,items):
    ratios = [(profit[i] / weight[i], i) for i in range(n)]
    ratios.sort()  # Sort items by profit-to-weight ratio (ascending order)

    min_profit = 0
    selected_items = []

    for ratio, i in ratios:
        if weight[i] <= cap:
            selected_items.append(items[i])
            min_profit += profit[i]
            cap -= weight[i]

    return min_profit, sorted(selected_items)




# Load the Excel file into a DataFrame
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
total_items = len(inventory_items)
total_cap = 11000
# max_value,items= dynamic_programming(total_cap, pack_sizes, unit_prices, total_items,inventory_items)
# print("Maximum value by Dynamic Programming:", max_value)
# print("Total items selected: ",len(items))
# # print(items)
# max_value1,items1= Greedy(total_cap, pack_sizes, unit_prices, total_items,inventory_items)
# print("Maximum value by Greedy:", max_value1)
# print("Total items selected: ",len(items1))
# print (items1)
# max_value1,items1= bruteforce(total_cap, pack_sizes, unit_prices,inventory_items,total_items)
# print("Maximum value by Brute force:", max_value1)
# print("Total items selected: ",len(items1))
# print(items1)

# if (items == items1):
#     print("yes they are same")
# write_items_to_file(items1, 'Final_list.txt')
# write_items_to_file(items, 'Final1_list.txt')

# Print or use the extracted information as needed
# print("Inventory Items:", inventory_items)
# print("Pack Sizes:", pack_sizes)
# print("Unit Prices:", unit_prices)


