# Stack using list

stack = []

# add items
stack.append("A")
stack.append("B")
stack.append("C")

print(stack)

# remove last item
last_item = stack.pop()
print(last_item)
print(stack)

# look at the top item
top_item = stack[-1]
print(top_item)


# Stack example: Reverse a string

stack = []
text = "hello"
reversed_text = ""

# Push all characters onto stack
for character in text:
    stack.append(character)

# Pop all characters
while len(stack) > 0:
    reversed_text += stack.pop()

print(reversed_text)


# Queue using list

queue = []

# add items
queue.append("D")
queue.append("E")
queue.append("F")

print(queue)

# dequeue (remove firt item or from the front)
first_char = queue.pop(0)
print(first_char)
print(queue)

'''Stack Practice Exerciese:'''
# Problem: Return True if the parentheses are balanced
stack = []
balanced_brackets = "(())"

for character in balanced_brackets:
    if character == "(":
        stack.append(character)
    elif character == ")":
        if len(stack) == 0:
            print("Not Balanced")
            break
        stack.pop()
else:
    print(len(stack) == 0)


# Problem: Reverse a list of numbers using a stack

stack = []
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []

for number in numbers:
    stack.append(number)

while len(stack) > 0:
    reversed_numbers.append(stack.pop())


print(numbers)
print(reversed_numbers)


'''Queue Practice Exercise:'''

# Problem: People enter a line are served in order.

queue = []
people = ["Isagi", "Aomine", "Nagi", "Izuku"]
served_people = []

for person in people:
    queue.append(person)

while len(queue) > 0:
    person = queue.pop(0)
    print(person, "is being served.")


# Problem: Return the first number that appears only once.

unique_num = [1, 1, 2, 2, 3, 4, 4, 5, 5]
count = {}
queue = []

for num in unique_num:
    if num not in count:
        count[num] = 1
        queue.append(num)
    else:
        count[num] += 1
    
while len(queue) > 0:
    if count[queue[0]] == 1:
        print(queue[0])
        break
    else:
        queue.pop(0)


