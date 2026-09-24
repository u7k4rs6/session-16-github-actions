"""A small calculator used to demonstrate GitHub Actions CI."""


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("cannot divide by zero")
    return left / right


def main() -> None:
    print("Simple Calculator")
    print("Use an expression such as 10 + 5, or enter q to quit.")

    while True:
        expression = input("Enter calculation: ").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            return

        parts = expression.split()
        if len(parts) != 3:
            print("Please use the format: number operator number")
            continue

        try:
            left, operator, right = float(parts[0]), parts[1], float(parts[2])
            operations = {
                "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide,
            }
            result = operations[operator](left, right)
        except (KeyError, ValueError) as error:
            print(f"Invalid calculation: {error}")
            continue

        print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
