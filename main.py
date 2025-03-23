from stats import *
import sys
def main():
    book_text = get_book_text()
    words_amount = count_words(book_text)
    characters_amount = count_characters(book_text)
    sorted_dictionarie = sort_dict(characters_amount)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {words_amount} total words
--------- Character Count -------""")
    
    for char_dict in sorted_dictionarie:
        character = char_dict['character']
        amount = char_dict['amount']
        
        # Only print if the character is alphabetic
        if character.isalpha():
            print(f"{character}: {amount}")
    
    print("============= END ===============")

main()