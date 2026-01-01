# Python (dict)
person = {
    "name": "Alice",
    "age": 25
}

print(person["name"])

person["age"] = 26
person["city"] = "London"

if "city" in person:
    print("City found")

print(person)

del person["city"]

print(person)



# Count letters in a string (HashMap)
def count_letters(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
    
print(count_letters("hello"))