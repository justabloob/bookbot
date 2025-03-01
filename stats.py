def count_words(text): # function to count the words in the text
    words = text.split() # split() splits the text into a list of words
    return len(words) # having the variable words makes it more readable and easier to modify later
    # len() counts the number of items in the list

def count_characters(text): # function to count the characters in the text
    lowered = text.lower() # lower() makes all the characters lowercase
    chars = {}
    for char in lowered:
        if char.isalpha(): # isalpha() checks if the character is a letter
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_characters(chars): # function to sort the characters by frequency
    return chars["num"]

def chars_dict_to_sorted_ls(chars_dict): # function to convert the dictionary to a list of dictionaries
    chars_ls = []
    for char in chars_dict:
        chars_ls.append({"char": char, "num": chars_dict[char]}) 
    chars_ls.sort(reverse=True, key=sort_characters) # sort the list of dictionaries by the value of the key "num"
    return chars_ls