# Map Coloring using Constraint Satisfaction Problem (CSP)

# Map represented as a graph
map_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']


def is_valid(region, color, assignment):
    # Check all neighboring regions
    for neighbor in map_graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False

    return True


def solve(assignment):
    # If all regions are colored
    if len(assignment) == len(map_graph):
        return assignment

    # Select an unassigned region
    for region in map_graph:
        if region not in assignment:
            break

    # Try each available color
    for color in colors:

        if is_valid(region, color, assignment):

            # Assign color
            assignment[region] = color

            # Recursively solve
            result = solve(assignment)

            if result:
                return result

            # Backtrack
            del assignment[region]

    return None


# Solve the map coloring problem
solution = solve({})


# Display the solution
if solution:
    print("Map Coloring Solution:")

    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution exists.")
