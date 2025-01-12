def main():
    book_path = "books/frankenstein.txt" # stablish the path to the book
    text = get_book_text(book_path) # get the text from the book
    word_count = count_words(text) # count the words in the text
    print(f"Word count: {word_count}")

def get_book_text(book_path): # function to get the text from the book
    with open(book_path) as f: # f is our opened file
        return f.read() # read() gets all the text and returns it

# is better to have several functions, following the separation of concerns principle
# this way, we can test eacht function separately 
# and we can reuse any function if needed to other purposes
# this way, we can also make the code more readable and maintainable
# and we can add more features easily

def count_words(text): # function to count the words in the text
    words = text.split() # split() splits the text into a list of words
    return len(words) # having the variable words makes it more readable and easier to modify later
    # len() counts the number of items in the list

main()
