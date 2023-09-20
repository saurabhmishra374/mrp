def max_duffel_bag_value(cake_tuples, capacity):
    # Initialize a list to store the maximum values for each capacity
    max_values = [0] * (capacity + 1)

    # Iterate through each cake type
    for cake_weight, cake_value in cake_tuples:
        # Check each capacity from 1 to the bag's capacity
        for current_capacity in range(1, capacity + 1):
            if cake_weight <= current_capacity:
                # Calculate the maximum value for the current capacity
                max_values[current_capacity] = max(
                    max_values[current_capacity],
                    max_values[current_capacity - cake_weight] + cake_value
                )

    # The maximum value for the bag's capacity is stored at the end of the list
    return max_values[capacity]

# Example usage:
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
result = max_duffel_bag_value(cake_tuples, capacity)
print(result)
