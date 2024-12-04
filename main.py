from collections import Counter


def count_words(book: str) -> int:
    return len(book.split())


def count_characters(book: str) -> Counter:
    return Counter(book.lower())


def main():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        book = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book)} words found in the document")
    print()
    counter = count_characters(book)
    for item in counter.most_common():
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
