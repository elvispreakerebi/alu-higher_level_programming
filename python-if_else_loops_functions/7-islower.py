#!/usr/bin/env python3
def islower(c):
    # Check if c is between 'a' and 'z' in ASCII values
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

# Test cases
print(f"a is {'lower' if islower('a') else 'upper'}")
print(f"H is {'lower' if islower('H') else 'upper'}")
print(f"A is {'lower' if islower('A') else 'upper'}")
print(f"3 is {'lower' if islower('3') else 'upper'}")
print(f"g is {'lower' if islower('g') else 'upper'}")
