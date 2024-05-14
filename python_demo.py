def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    """Main function."""
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
