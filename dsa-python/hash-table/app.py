# Count Character Frequencies in a String

# Problem 1: Given a string, count how many times each character appears.


def character_frequencies(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency

print(character_frequencies("banana"))   # output: banana = {"b": 1, "a": 3, "n": 2}

print(character_frequencies("Pineapple"))   # output: Pineapple = {'P': 1, 'i': 1, 'n': 1, 'e': 2, 'a': 1, 'p': 2, 'l': 1}

print(character_frequencies("Mango"))   # output: Mango = {'M': 1, 'a': 1, 'n': 1, 'g': 1, 'o': 1}



# Problem 2: Given a list of numbers, return the first duplicate you encounter.

def first_duplicate(numbers):
    numbers_seen = {}

    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen[number] = True
    
    return None

print(first_duplicate([2, 5, 1, 2, 3, 5]))  # output: 2

print(first_duplicate([10, 3, 5, 3, 5, 1, 9]))   # ouput: 3. --- 3 is the first duplicate that is in the list at index 1 & 3. Second duplicate is 5 at index 2 & 4 but that doesn't count because we are finding the first duplicate in the list.



# Problem 3: Return True if two words contain the same letters in the same frequency. (anagrams)

def have_same_letters(word1, word2):
    if len(word1) != len(word2):
        return False
    
    count = {}

    for character in word1:
        count[character] = count.get(character, 0) + 1

    for character in word2:
        if character not in count or count[character] == 0:
            return False
        else:
            count[character] -= 1
        
    return True

print(have_same_letters("listen", "silent"))   # output: True

print(have_same_letters("sore", "rose"))   # output: True

print(have_same_letters("faster", "master"))   # output: False


# Problem 4: Write a function that returns the first non-repeating character in a string.

def first_unique_character(text):
    unique_char_count = {}

    for character in text:
        if character in unique_char_count:
            unique_char_count[character] += 1
        else:
            unique_char_count[character] = 1

    # Shortcut using get() method
    # for character in text:
    #     unique_char_count[character] = unique_char_count.get(character, 0) + 1
        

    for character in text:
        if unique_char_count[character] == 1:
            return character
    
    return None    # in case no unique character is exists
    
print(first_unique_character("swiss"))  # output: w

print(first_unique_character("repeater"))  # output: p