def UnCorrect(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            stack.append(char)
    return not stack


a = input()
b = input()
print(UnCorrect(a))
print(UnCorrect(b))
