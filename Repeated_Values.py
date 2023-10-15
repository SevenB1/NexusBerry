import random
def count_repeated_elements(my_tuple):
    counts = {}
    for item in my_tuple:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    result = [(item, count) for item, count in counts.items() if count > 1]
    return tuple(result)

# Function to generate a random tuple with specified length and range of values
def generate_random_tuple(length, min_value, max_value):
    return tuple(random.randint(min_value, max_value) for _ in range(length))

# Generate a random tuple with 20 elements ranging from 1 to 100
random_tuple = generate_random_tuple(20, 1, 100)

# Print the generated random tuple
print("Random Tuple:", random_tuple)

# Find and print the repeated elements
result = count_repeated_elements(random_tuple)
print("Repeated Elements:", result)
