from itertools import permutations

# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ['A', 'B', 'C', 'D']

start_city = 0
minimum_distance = float('inf')
best_route = []

# Generate all possible routes
for route in permutations(range(1, len(cities))):

    current_route = (start_city,) + route + (start_city,)

    total_distance = 0

    for i in range(len(current_route) - 1):
        total_distance += distance[
            current_route[i]
        ][
            current_route[i + 1]
        ]

    # Check for minimum distance
    if total_distance < minimum_distance:
        minimum_distance = total_distance
        best_route = current_route

# Display result
print("Best Route:")

for i in range(len(best_route)):
    print(cities[best_route[i]], end="")

    if i < len(best_route) - 1:
        print(" -> ", end="")

print("\nMinimum Distance:", minimum_distance)
