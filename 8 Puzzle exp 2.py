import heapq

# Goal state
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible movements of the blank space
MOVES = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}


def manhattan_distance(state):
    """Calculate Manhattan distance heuristic."""
    distance = 0

    for index, value in enumerate(state):
        if value != 0:
            goal_index = GOAL_STATE.index(value)

            current_row = index // 3
            current_col = index % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    """Generate all possible next states."""
    neighbors = []

    zero_index = state.index(0)
    row = zero_index // 3
    col = zero_index % 3

    # Up
    if row > 0:
        new_index = zero_index - 3
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = \
            new_state[new_index], new_state[zero_index]
        neighbors.append((tuple(new_state), "Up"))

    # Down
    if row < 2:
        new_index = zero_index + 3
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = \
            new_state[new_index], new_state[zero_index]
        neighbors.append((tuple(new_state), "Down"))

    # Left
    if col > 0:
        new_index = zero_index - 1
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = \
            new_state[new_index], new_state[zero_index]
        neighbors.append((tuple(new_state), "Left"))

    # Right
    if col < 2:
        new_index = zero_index + 1
        new_state = list(state)
        new_state[zero_index], new_state[new_index] = \
            new_state[new_index], new_state[zero_index]
        neighbors.append((tuple(new_state), "Right"))

    return neighbors


def solve_puzzle(start_state):
    # Priority queue: (f_cost, g_cost, state, path)
    priority_queue = []

    h_cost = manhattan_distance(start_state)

    heapq.heappush(
        priority_queue,
        (h_cost, 0, start_state, [])
    )

    visited = set()

    while priority_queue:
        f_cost, g_cost, current_state, path = \
            heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)

        # Goal reached
        if current_state == GOAL_STATE:
            return path, current_state

        # Generate next states
        for next_state, move in get_neighbors(current_state):

            if next_state not in visited:
                new_g_cost = g_cost + 1
                new_h_cost = manhattan_distance(next_state)
                new_f_cost = new_g_cost + new_h_cost

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_cost,
                        new_g_cost,
                        next_state,
                        path + [move]
                    )
                )

    return None, None


def print_state(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        print(
            "| {} | {} | {} |".format(
                state[i] if state[i] != 0 else " ",
                state[i + 1] if state[i + 1] != 0 else " ",
                state[i + 2] if state[i + 2] != 0 else " "
            )
        )
        print("+---+---+---+")


# Main program
print("Enter the 8-puzzle values")
print("Use 0 for the blank space")

start_state = tuple(
    map(int, input("Enter 9 numbers separated by spaces: ").split())
)

print("\nInitial State:")
print_state(start_state)

moves, final_state = solve_puzzle(start_state)

if moves:
    print("\nSolution Found!")
    print("Number of moves:", len(moves))
    print("Moves:", " -> ".join(moves))

    print("\nFinal State:")
    print_state(final_state)
else:
    print("\nNo solution found.")
