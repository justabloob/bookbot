def main():
    with open("books/frankenstein.txt") as f:
        for line in f:
            print(line.strip())

main()