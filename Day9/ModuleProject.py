#1. Generate random numbers
#2. Check which numbers are even_odd
#3. Round numbers using math
#4. count how many times numbers appears
#5. save the result in file

import random
import math
from collections import Counter
import os

# 1. Generate random numbers
print("Generating 10 random numbers between 1 and 100:")
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Generated Numbers: {random_numbers}")

results = []
results.append("Generated Numbers and Analysis:")
results.append(f"Generated Numbers: {random_numbers}")

# 2. Check which numbers are even_odd and 3. Round numbers using math
print("\nAnalyzing numbers for even/odd and rounding:")
for num in random_numbers:
    even_odd = "Even" if num % 2 == 0 else "Odd"
    floor_num = math.floor(num)
    ceil_num = math.ceil(num)
    rounded_num = round(num)
    analysis = f"Number: {num}, Status: {even_odd}, Floor: {floor_num}, Ceil: {ceil_num}, Rounded: {rounded_num}"
    print(analysis)
    results.append(analysis)

# 4. Count how many times numbers appears
print("\nCounting occurrences of each number:")
number_counts = Counter(random_numbers)
print(f"Number Counts: {number_counts}")
results.append(f"\nNumber Counts: {number_counts}")

# 5. Save the result in file
file_name = "random_number_analysis.txt"

# Create 'myfolder' if it doesn't exist (assuming it's where other files are created)
folder_name = "myfolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")

file_path = os.path.join(folder_name, file_name)

try:
    with open(file_path, "w") as f:
        for line in results:
            f.write(line + "\n")
    print(f"\nResults successfully saved to '{file_path}'")
except IOError as e:
    print(f"Error saving file: {e}")









#