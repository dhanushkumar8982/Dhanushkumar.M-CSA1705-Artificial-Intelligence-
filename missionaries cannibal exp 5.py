from collections import deque

def is_valid(state):
    missionaries_left, cannibals_left, boat = state

    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # Values cannot be negative or exceed 3
    if not (0 <= missionaries_left <= 3 and
            0 <= cannibals_left <= 3):
        return False

    # Check left bank
    if missionaries_left > 0 and \
       cannibals_left > missionaries_left:
        return False

    # Check right bank
    if missionaries_right > 0 and \
       cannibals_right > missionaries_right:
        return False

    return True


def get_next_states(state):
    missionaries, cannibals, boat = state

    possible_moves = [
        (1, 0),  # 1 Missionary
        (2, 0),  # 2 Missionaries
        (0, 1),  # 1 Cannibal
        (0, 2),  # 2 Cannibals
        (1, 1)   # 1 Missionary and 1 Cannibal
    ]

    next_states = []

    for m, c in possible_moves:

        if boat == 0:  # Boat on the left bank
            new_state = (
                missionaries - m,
                cannibals - c,
                1
            )
        else:  # Boat on the right bank
            new_state = (
                missionaries + m,
                cannibals + c,
                0
            )

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


def solve():
    # State format:
    # (Missionaries on left, Cannibals on left, Boat position)
    # Boat: 0 = Left, 1 = Right

    start_state = (3, 3, 0)
    goal_state = (0, 0, 1)

    queue = deque()
    queue.append((start_state, [start_state]))

    visited = set()
    visited.add(start_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for next_state in get_next_states(current_state):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [next_state])
                )

    return None


def print_solution(solution):
    print("Solution Found!\n")

    for step, state in enumerate(solution):
        missionaries, cannibals, boat = state

        boat_position = "Left Bank" if boat == 0 else "Right Bank"

        print(
            f"Step {step}: "
            f"Missionaries on Left = {missionaries}, "
            f"Cannibals on Left = {cannibals}, "
            f"Boat = {boat_position}"
        )


solution = solve()

if solution:
    print_solution(solution)
else:
    print("No solution exists.")
