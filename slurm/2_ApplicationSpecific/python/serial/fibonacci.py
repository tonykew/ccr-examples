def fib(n: int) -> int:
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

if __name__ == "__main__":

    print(f"Fibonacci number at position 7 is: {fib(7)}")
    print(f"Fibonacci number at position 20 is: {fib(20)}")


