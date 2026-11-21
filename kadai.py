import sys

def multiply_tokens(tokens: list[str]) -> float | int:
    if len(tokens) < 2:
        raise ValueError("Please provide two numbers.")
    a = float(tokens[0])
    b = float(tokens[1])
    prod = a * b
    if prod.is_integer():
        return int(prod)
    return prod

def main() -> None:
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    result = multiply_tokens(tokens)
    sys.stdout.write(f"{result}\n")

if __name__ == "__main__":
    main()
