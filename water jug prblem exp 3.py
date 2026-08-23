from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    start = (0, 0)

    queue = deque()
    queue.append((start, []))

    visited = set()

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        path = path + [(jug1, jug2)]

        # Check whether target amount is reached
        if jug1 == target or jug2 == target:
            return path

        states = []

        # Fill Jug 1
        states.append((jug1_capacity, jug2))

        # Fill Jug 2
        states.append((jug1, jug2_capacity))

        # Empty Jug 1
        states.append((0, jug2))

        # Empty Jug 2
        states.append((jug1, 0))

        # Pour Jug 1 into Jug 2
        amount = min(jug1, jug2_capacity - jug2)
        states.append((jug1 - amount, jug2 + amount))

        # Pour Jug 2 into Jug 1
        amount = min(jug2, jug1_capacity - jug1)
        states.append((jug1 + amount, jug2 - amount))

        for state in states:
            if state not in visited:
                queue.append((state, path))

    return None


# Get input from user
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

# Solve the problem
solution = water_jug_problem(
    jug1_capacity,
    jug2_capacity,
    target
)

# Display result
if solution:
    print("\nSolution Steps:")

    for step, state in enumerate(solution):
        print(
            f"Step {step}: "
            f"Jug 1 = {state[0]} gallons, "
            f"Jug 2 = {state[1]} gallons"
        )
else:
    print("\nNo solution exists.")
