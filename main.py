def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)

def get_text(book_path):
    with open(book_path) as f:
        return f.read()

main()
