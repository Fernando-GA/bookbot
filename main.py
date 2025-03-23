from stats import *
def main():
    book_text = get_book_text("books/frankenstein.txt")
    words_amount = count_words(book_text)
    print(f"{words_amount} words found in the document")

main()
