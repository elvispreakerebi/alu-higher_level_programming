#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')

# Test case (for standalone testing)
if __name__ == "__main__":
    fizzbuzz()
    print("")  # To ensure the prompt appears on the next line
