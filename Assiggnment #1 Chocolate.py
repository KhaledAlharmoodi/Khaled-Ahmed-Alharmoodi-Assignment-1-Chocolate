import time
import matplotlib.pyplot as plt  

# Task one
class Chocolates: # chocolate class
    def __init__(self, weight, price, types, ID): # attributes of the class
        self.weight = weight
        self.price = price
        self.types = types
        self.ID = ID

def iterativeChocDist(chocolates, students): # the first way of distributing the chocolates for the students
    distributed_chocolates = [] # chocolate list
    for i in range(len(students)): # for loop
        if i < len(chocolates): # if statement
            distributed_chocolates.append((students[i], chocolates[i]))
        else:
            break # stop the for loop
    return distributed_chocolates

def distribute_chocolates_recursive(chocolates, students, index=0): # the second way of distributing the chocolates for the students
    if index >= len(students) or index >= len(chocolates): # if statement
        return []
    else:
        return [(students[index], chocolates[index])] + distribute_chocolates_recursive(chocolates, students, index + 1)

# Test cases
chocolates = [Chocolates(3, 1, "Milk Chocolate", "001"),
    Chocolates(4, 2, "Carmel Chocolate", "002"),
    Chocolates(1, 4, "Dark Chocolate", "003"),
    Chocolates(2, 3, "White Chocolate", "004"),
    Chocolates(5, 9, "Hazelnut Chocolate", "005"),
    Chocolates(6, 7, "Pumpkin Chocolate", "006"),
    Chocolates(7, 10, "Mint Chocolate", "007"),
    Chocolates(9, 6, "Almond Chocolate", "008"),
    Chocolates(3, 7, "Pistachio Chocolate", "009"),
    Chocolates(8, 8, "Bubbld Chocolate", "010"),]

students = ["Khaled", "Mohammed", "Hamad", "Rashed", "Saif", "Sultan", "Fares", "Abdulla", "Ahmed", "Saeed"]

# Iterative Distribution with timer
start_time = time.time() # will start counting the time
iterative_dist = iterativeChocDist(chocolates, students) # will start counting the time while distributing the chocolate iteratively
end_time = time.time() # will stop the timer

print("Iterative Distribution:")
for student, chocolate in iterative_dist:
    print(f"{student} gets {chocolate.types}")

print(f"\nTime taken for iterative distribution: {end_time - start_time} seconds")

# Recursive Distribution with timer
start_time = time.time() # will start counting the time
recursive_distribution = distribute_chocolates_recursive(chocolates, students) # will start counting the time while distributing the chocolate recursively
end_time = time.time() # will stop the timer

print("\nRecursive Distribution:")
for student, chocolate in recursive_distribution:
    print(f"{student} gets {chocolate.types}")

print(f"\nTime taken for recursive distribution: {end_time - start_time} seconds")

# Complexity Analysis
# O(n) for Big O notation: The time complexity of the iterative and recursive distribution algorithms is linear and is denoted by O(n) in the comment "Use O(n) for the Big O notation." The notation O(n), where n is the amount of the input, indicates that the time required by these methods increases linearly with the size of the input data (in this case, the number of students). This implies that the time it takes the algorithms to distribute chocolates will grow in direct proportion to the number of students.
# Time Complexity: The time complexity of the recursive and iterative functions is O(min(n, m)), where n and m are the number of students and chocolates, respectively. This is because the best-case, average-case, and worst-case possibilities are the same when we cycle through the students list or the chocolates list until we exhaust the smaller list. iterative and recursive distribution algorithms have a time complexity of O(n) in the best, average, and worst-case scenarios, where n is the number of students.
# Space Complexity: Since both functions just store the dispersed chocolates in a list, their space complexity is O(min(n, m)). The number of distributed chocolates, which is constrained by the smaller of the two input lists, determines the spatial complexity.

# Task two
def sort_chocolates_by_weight(chocolates): # sorting the chocolates by weight
    return sorted(chocolates, key=lambda x: x.weight)

def sort_chocolates_by_price(chocolates): # sorting the chocolates by price
    return sorted(chocolates, key=lambda x: x.price)

# Test cases
start_time = time.time() # will start counting the time
sorted_by_weight = sort_chocolates_by_weight(chocolates) # the timer will count the time until the algorithm will sort the chocolates by weight
end_time = time.time() # timer will stop

print("Chocolates sorted by weight:")
for chocolate in sorted_by_weight:
    print(f"Type: {chocolate.types}, Weight: {chocolate.weight}")

print(f"\nTime taken for sorting chocolates by weight: {end_time - start_time} seconds")

start_time = time.time() # will start counting the time
sorted_by_price = sort_chocolates_by_price(chocolates) # the timer will count the time until the algorithm will sort the chocolates by price
end_time = time.time() # timer will stop

print("\nChocolates sorted by price:")
for chocolate in sorted_by_price:
    print(f"Type: {chocolate.types}, Price: {chocolate.price}")

print(f"\nTime taken for sorting chocolates by price: {end_time - start_time} seconds")

# Justification for sorting algorithm choice: We have chosen Python's built-in sorted() function which uses Timsort, a hybrid sorting algorithm derived from merge sort and insertion sort. Timsort is a very effective method for sorting a lot of chocolates since it has a time complexity of O(n log n) in both average and worst-case situations.
# Efficiency discussion: Timsort's efficiency stays optimal with a time complexity of O(n log n) even if the number of chocolates and pupils increases dramatically. This is due to the fact that Timsort works well with partially sorted arrays, which can happen while giving students chocolates. As a result, even with a big input size, the method is still efficient.
# Complexity analysis: Sorting chocolates by price and weight has a time complexity of O(n log n) since the time complexity of Timsort (used in Python's sorted() function) is O(n log n) on average and worst-case situations. Since more space is needed to keep the sorted lists, the space complexity for both sorting processes is O(n), where n is the number of chocolates.

import time
#Task three
def chocolate_price_search(chocolates, price):  #searching chocolate by price
    for student, chocolate in chocolates: #for loop
        if chocolate.price == price: #if statment
            return student
    return None

def chocolate_weight_search(chocolates, weight):  #searching chocolate by weight
    for student, chocolate in chocolates: #for loop
        if chocolate.weight == weight: # if statement
            return student
    return None


# Test cases
price = 4 # Use the same price variable as in Task one
start_time = time.time()
StudentSpecifiedPrice = chocolate_price_search(iterative_dist, price)
end_time = time.time()
StudentSpecifiedPrice = chocolate_price_search(iterative_dist, price)
if StudentSpecifiedPrice:
    print(f"The student who is holding a chocolate with price {price} is: {StudentSpecifiedPrice}")
else:
    print(f"No student is found holding a chocolate with price {price}")
print(f"Time taken for searching chocolates by price: {end_time - start_time} seconds")

weight = 7 # Use the same weight variable as in Task one
start_time = time.time()
StudentSpecifiedWeight = chocolate_weight_search(iterative_dist, weight)
end_time = time.time()
StudentSpecifiedWeight = chocolate_weight_search(iterative_dist, weight)
if StudentSpecifiedWeight:
    print(f"The student who is holding a chocolate with weight {weight} is: {StudentSpecifiedWeight}")
else:
    print(f"No student is found holding a chocolate with weight {weight}")
print(f"Time taken for searching chocolates by weight: {end_time - start_time} seconds")

# Graph one
# T(n) of iterative distribution
def iterativeChocDist(n):
    # simulate distribution with n students and n chocolates
    students = list(range(n))
    chocolates = list(range(n))
    return students, chocolates

# T(n) of recursive distribution
def distribute_chocolates_recursive(n):
    # simulate distribution with n students and n chocolates
    students = list(range(n))
    choco = list(range(n))
    return students, choco

input_size = list(range(1, 1001, 100))
iterative_t = []
recursive_t = []

for size in input_size:
    #time for iterative distribution
    start = time.time()
    iterativeChocDist(size)
    end = time.time()
    iterative_t.append(end - start)

    # time for recursive distribution
    start = time.time()
    distribute_chocolates_recursive(size)
    end = time.time()
    recursive_t.append(end - start)

# plot the graph
plt.figure(figsize=(10, 6))
plt.plot(input_size, iterative_t, label='Iterative Distribution')
plt.plot(input_size, recursive_t, label='Recursive Distribution')
plt.xlabel('Number of Students/Chocolates')
plt.ylabel('Time (s)')
plt.title('Time Complexity: Iterative vs Recursive')
plt.legend()
plt.show()
# explaining: When the time complexity for both iterative distribution and recursive distribution is O(n log n), it means that the time taken to distribute chocolates among students using either method grows in proportion to the number of students (n) but with a logarithmic factor.

#Graph two

# Define functions to sort chocolates by weight and price
def sort_chocolates_by_weight(chocolates):
    start = time.time()
    sorted_chocolates = sorted(chocolates, key=lambda x: x.weight)
    end = time.time()
    return end - start

def sort_chocolates_by_price(chocolates):
    start = time.time()
    sorted_chocolates = sorted(chocolates, key=lambda x: x.price)
    end = time.time()
    return end - start

# Vary input size and measure time taken for each sorting method
input_sizes = list(range(1, 1001, 100))
weight_sort_times = []
price_sort_times = []

for size in input_sizes:
    choc = [Chocolates(weight=i, price=0, types="", ID="") for i in range(size)]

    # Time taken for sorting chocolates by weight
    weight_sort_times.append(sort_chocolates_by_weight(choc))

    # Time taken for sorting chocolates by price
    price_sort_times.append(sort_chocolates_by_price(choc))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, weight_sort_times, label='Sort by Weight')
plt.plot(input_sizes, price_sort_times, label='Sort by Price')
plt.xlabel('Input Number of Chocolates')
plt.ylabel('Time T(s)')
plt.title('Time Complexity: Sorting Chocolates')
plt.legend()
plt.grid(True)
plt.show()

#sorting chocolates with O(nlogn) time complexity means that the sorting algorithm is efficient and can handle larger inputs relatively quickly compared to algorithms with higher time complexities
#graph three

# Function to simulate searching chocolates by price
def chocolate_price_search(chocolates, index):
    start = time.time()
    for _ in range(10):  # Performing the search operation multiple times for accurate measurement
        chocolates[index]
    end = time.time()
    return (end - start) / 10  # Taking average time

# Function to simulate searching chocolates by weight
def chocolate_weight_search(chocolates, index):
    start = time.time()
    for _ in range(10):  # Performing the search operation multiple times for accurate measurement
        chocolates[index]
    end = time.time()
    return (end - start) / 10  # Taking average time

# Vary input size and measure time taken for each searching method
input_sizes = list(range(1, 1001, 100))
price_search_times = []
weight_search_times = []

for size in input_sizes:
    chocolates = [(None, Chocolates(weight=i, price=i, types="", ID="")) for i in range(size)]
    index = size - 1  # Searching for the highest index
    # Time taken for searching chocolates by price
    price_search_times.append(chocolate_price_search(chocolates, index))

    # Time taken for searching chocolates by weight
    weight_search_times.append(chocolate_weight_search(chocolates, index))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, price_search_times, label='Search by Price')
plt.plot(input_sizes, weight_search_times, label='Search by Weight')
plt.xlabel('Input Number of Chocolates')
plt.ylabel('Time (s)')
plt.title('Time Complexity: Searching Chocolates')
plt.legend()
plt.grid(True)
plt.show()

# Searching by Price O(nlogn): As the number of chocolates (n) increases, the time it takes to find a chocolate by its price grows moderately. It's efficient but not as fast as some other algorithms.

# Searching by Weight  O(logn)): When looking for chocolates by weight, as the number of chocolates increases, the time it takes to find a chocolate grows very slowly. It's highly efficient even with a large number of chocolates.