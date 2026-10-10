import itertools

transactions = [
    ["Bread", "Milk", "Eggs"],
    ["Bread", "Diapers", "Beer"],
    ["Milk", "Diapers", "Beer", "Eggs"],
    ["Bread", "Milk", "Diapers", "Beer"],
    ["Bread", "Milk", "Diapers"],
    ["Milk", "Eggs"]
]

def calculate_support(item, transactions):
    count = sum(1 for basket in transactions if item in basket)
    return count / len(transactions)

def calculate_pair_support(item_a, item_b, transactions):
    count = sum(1 for basket in transactions if item_a in basket and item_b in basket)
    return count / len(transactions)

def calculate_confidence(item_a, item_b, transactions):
    return calculate_pair_support(item_a, item_b, transactions) / calculate_support(item_a, transactions)

def calculate_lift(item_a, item_b, transactions):
    return calculate_confidence(item_a, item_b, transactions) / calculate_support(item_b, transactions)

all_items = set(item for basket in transactions for item in basket)
item_pairs = list(itertools.combinations(all_items, 2))

print("Item Pair Analysis:")
for item_a, item_b in item_pairs:
    support_pair = calculate_pair_support(item_a, item_b, transactions)
    if support_pair > 0:
        confidence = calculate_confidence(item_a, item_b, transactions)
        lift = calculate_lift(item_a, item_b, transactions)
        print(f"{item_a} -> {item_b}: Support={support_pair:.2f}, Confidence={confidence:.2f}, Lift={lift:.2f}")