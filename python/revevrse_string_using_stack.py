import list_stack as stack

string = "Hi, My name is Jeet and I am preparing for competitive programming"

reverse_string = ""

s = stack.Stack()

for char in string:
    s.push(char)

while not s.in_empty():
    reverse_string = reverse_string + s.pop()

print(reverse_string)