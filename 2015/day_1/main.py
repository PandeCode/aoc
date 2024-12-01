def solve(data):
    floor = 0
    for c in data:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


print(solve("(())"), 0) 
print(solve("()()"), 0)
print(solve("((("), 3) 
print(solve("(()(()("), 3)
print(solve("())"), -1) 
print(solve("))("), -1)
print(solve(")))"), -3) 
print(solve(")())())"), -3)
print(solve("))(((((") , 3)

assert(solve("(())")== 0) 
assert(solve("()()")== 0)
assert(solve("(((")== 3) 
assert(solve("(()(()(")== 3)
assert(solve("())")== -1) 
assert(solve("))(")== -1)
assert(solve(")))")== -3) 
assert(solve(")())())")== -3)
assert(solve("))(((((") == 3)

with open("input") as file:
    data = file.read()

print(solve(data))
