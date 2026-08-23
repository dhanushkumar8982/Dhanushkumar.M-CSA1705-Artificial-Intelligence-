from itertools import permutations

def solve_cryptarithmetic():
    letters = "SENDMORY"

    # M cannot be 0 because it is the first digit of MONEY
    for digits in permutations(range(10), len(letters)):

        mapping = dict(zip(letters, digits))

        # Leading letters cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND = (
            mapping['S'] * 1000 +
            mapping['E'] * 100 +
            mapping['N'] * 10 +
            mapping['D']
        )

        MORE = (
            mapping['M'] * 1000 +
            mapping['O'] * 100 +
            mapping['R'] * 10 +
            mapping['E']
        )

        MONEY = (
            mapping['M'] * 10000 +
            mapping['O'] * 1000 +
            mapping['N'] * 100 +
            mapping['E'] * 10 +
            mapping['Y']
        )

        if SEND + MORE == MONEY:
            print("Solution Found!")
            print(mapping)
            print()
            print(f"  {SEND}")
            print(f"+ {MORE}")
            print("--------")
            print(f" {MONEY}")
            return

    print("No solution found.")


solve_cryptarithmetic()
