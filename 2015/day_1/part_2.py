def solve(data):
    floor = 0
    for i, c in enumerate(data):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
            if floor == -1:
                return i + 1
        

print(solve(")"), 1) 
print(solve("()())") , 5)

assert(solve(")")== 1) 
assert(solve("()())") == 5)

with open("input") as file:
    data = file.read()

print(solve(data))
