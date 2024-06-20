#!/usr/bin/python3


def pow(a, b):
    result = 1  # Initialize result to 1 (since any number to the power of 0 is 1)
    if b == 0:
        return result
    elif b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result

# Test cases (for standalone testing)
if __name__ == "__main__":
    print(pow(2, 3))    # Should print 8
    print(pow(5, 0))    # Should print 1
    print(pow(2, -3))   # Should print 0.125
    print(pow(10, 2))   # Should print 100)
