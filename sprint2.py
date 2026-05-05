# IT 3883 Final Exam - Coin to Dollar Converter
# Author: Jermaine Ayuk
# Description: Converts pseudo-English coin statements into dollar amounts.
# Sprint 2 - Corrected Implementation

def coin_to_dollar(sentence):
    coin_values = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25
    }

    # Map plural forms to singular denominations
    plural_map = {
        "pennies": "penny",
        "nickels": "nickel",
        "dimes": "dime",
        "quarters": "quarter"
    }

    total = 0.0
    parts = sentence.lower().replace(",", " ").split("and")

    for part in parts:
        words = part.strip().split()
        if len(words) >= 2:
            quantity = int(words[0])
            denomination = plural_map.get(words[1], words[1])  # normalize plural forms
            if denomination in coin_values:
                total += quantity * coin_values[denomination]
            else:
                print(f"Unknown denomination: {denomination}")
    return round(total, 2)

# Test cases
tests = [
    "1 penny and 2 nickels",
    "4 dimes and 7 quarters",
    "1 quarter and 3 pennies",
    "21 pennies and 17 dimes and 52 quarters",
    "95 dimes and 73 quarters and 22 nickels and 36 pennies",
    "1 nickel and 17 quarters",
    "21 nickels and 15 pennies",
    "1 dime and 1 nickel and 1 penny and 1 quarter"
]

for t in tests:
    print(f"{t} -> ${coin_to_dollar(t):.2f}")
