# is better to have several functions, following the separation of concerns principle
# this way, we can test eacht function separately 
# and we can reuse any function if needed to other purposes
# this way, we can also make the code more readable and maintainable
# and we can add more features easily

def main():
    book_path = "books/frankenstein.txt" # stablish the path to the book
    text = get_book_text(book_path) # get the text from the book
    word_count = count_words(text) 
    characters = count_characters(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(chars_ls)

def get_book_text(book_path): # function to get the text from the book
    with open(book_path) as f: # f is our opened file
        return f.read() # read() gets all the text and returns it

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

# Create a dictionary of character frequencies
chars = count_characters("Counting characters")

# Convert dictionary to a list of dictionaries
chars_ls = [{"char": char, "num": count} for char, count in chars.items()]

def sort_characters(chars): # function to sort the characters by frequency
    return chars["num"]

chars_ls.sort(reverse=True, key=sort_characters)


main()