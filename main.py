def main():
    book_path = "books/frankenstein.txt" # stablish the path to the book
    text = get_book_text(book_path) # get the text from the book
    print(text)

def get_book_text(book_path): # function to get the text from the book
    with open(book_path) as f: # f is our opened file
        return f.read() # read() gets all the text and returns it

# is better to have two functions, following the separation of concerns principle
# this way, we can test the get_book_text function separately from the main function
# and we can reuse the get_book_text function if we need to get the text from another book
# also if we need to change how read files, we only need to change the get_book_text function

main()
