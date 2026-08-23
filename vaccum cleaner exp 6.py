# Vacuum Cleaner Problem

def vacuum_cleaner(room_a, room_b, vacuum_position):

    print("Initial State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", vacuum_position)

    print("\nActions:")

    # If vacuum is in Room A
    if vacuum_position == "A":

        if room_a == "Dirty":
            print("Action: Clean Room A")
            room_a = "Clean"

        print("Action: Move to Room B")
        vacuum_position = "B"

        if room_b == "Dirty":
            print("Action: Clean Room B")
            room_b = "Clean"

    # If vacuum is in Room B
    else:

        if room_b == "Dirty":
            print("Action: Clean Room B")
            room_b = "Clean"

        print("Action: Move to Room A")
        vacuum_position = "A"

        if room_a == "Dirty":
            print("Action: Clean Room A")
            room_a = "Clean"

    print("\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", vacuum_position)


# Get input from the user
room_a = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_b = input("Enter status of Room B (Clean/Dirty): ").capitalize()
vacuum_position = input("Enter vacuum position (A/B): ").upper()

# Solve the problem
vacuum_cleaner(room_a, room_b, vacuum_position)
