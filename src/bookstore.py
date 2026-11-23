"""Quote book orders using whole cents."""
import argparse

CATALOG = {"python": 2500, "algorithms": 4000}


def quote(title, quantity):
    if title not in CATALOG:
        raise ValueError("Unknown book")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return CATALOG[title] * quantity


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title")
    parser.add_argument("quantity", type=int)
    args = parser.parse_args()
    try:
        cents = quote(args.title, args.quantity)
    except ValueError as error:
        parser.exit(2, f"{error}\n")
    print(f"Total: ${cents // 100}.{cents % 100:02d}")


if __name__ == "__main__":
    main()
