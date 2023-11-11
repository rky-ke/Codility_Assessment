# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    if not S:
        return ""
    stack = []

    for char in S:
        if stack and ((char == 'A' and stack[-1] == 'B') or (char == 'B' and stack[-1] == 'A')):
            # Remove pair
            stack.pop()
        elif stack and ((char == 'C' and stack[-1] == 'D') or (char == 'D' and stack[-1] == 'C')):
            # Remove C and D pair
            stack.pop()
        else:
            # Add current characters to the stack
            stack.append(char)
    # Return the rmaining characters in the stack as the result
    result = ''.join(stack)
    print(f"Final Result: {result}")
    return result


# Read input from test-input.txt
if __name__ == "__main__":
    with open("test-input.txt", "r") as file:
        input_string = file.read().strip()
    result = solution(input_string)
    print(result)