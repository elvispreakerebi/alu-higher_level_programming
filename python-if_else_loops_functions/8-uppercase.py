#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        # Convert lowercase letters to uppercase by adjusting ASCII values
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

# Test cases (for standalone testing)
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
