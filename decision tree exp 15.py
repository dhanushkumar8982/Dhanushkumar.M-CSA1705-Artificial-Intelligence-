import math
from collections import Counter


# Calculate Entropy
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)

    counts = Counter(labels)

    entropy_value = 0

    for count in counts.values():
        probability = count / total
        entropy_value -= probability * math.log2(probability)

    return entropy_value


# Calculate Information Gain
def information_gain(data, attribute_index):
    total_entropy = entropy(data)

    values = set(row[attribute_index] for row in data)

    weighted_entropy = 0

    for value in values:
        subset = [
            row for row in data
            if row[attribute_index] == value
        ]

        weighted_entropy += (
            len(subset) / len(data)
        ) * entropy(subset)

    return total_entropy - weighted_entropy


# Build Decision Tree
def build_tree(data, attributes):

    labels = [row[-1] for row in data]

    # If all labels are the same
    if len(set(labels)) == 1:
        return labels[0]

    # If no attributes are left
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    # Select attribute with maximum information gain
    best_attribute = max(
        attributes,
        key=lambda index: information_gain(data, index)
    )

    tree = {
        best_attribute: {}
    }

    values = set(row[best_attribute] for row in data)

    remaining_attributes = [
        attribute for attribute in attributes
        if attribute != best_attribute
    ]

    for value in values:

        subset = [
            row for row in data
            if row[best_attribute] == value
        ]

        if subset:
            tree[best_attribute][value] = build_tree(
                subset,
                remaining_attributes
            )

    return tree


# Training Dataset
# [Outlook, Temperature, Play]
data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rainy', 'Cool', 'Yes'],
    ['Rainy', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Overcast', 'Cool', 'Yes']
]


# Attributes: Outlook and Temperature
attributes = [0, 1]

# Build the Decision Tree
decision_tree = build_tree(data, attributes)

print("Decision Tree:")
print(decision_tree)
