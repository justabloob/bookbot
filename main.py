def main():
    line_count = 0
    with open("books/frankenstein.txt") as f:
        for line in f:
            print(line.strip())
            line_count += 1
    print(f"Line count: {line_count}")
main()