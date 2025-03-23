def get_book_text(filepath):
    file_content = ""
    with open(filepath) as f:
        file_content= f.read()
    return file_content

def count_words(text):
    num_of_words = text.split()
    num_of_words = len(num_of_words)
    
    return num_of_words 

def count_characters(text):
    text_to_low = text.lower()
    total_char = {}
    for char in text_to_low:
        if char not in total_char:
            total_char[char] = 1
        else:
            total_char[char] += 1

    return total_char

def sort_on(dict):
    return dict["amount"]

def sort_dict(char_dict):
    dictionarie_list = []
    for char in char_dict:
        value = char_dict[char]
        dictionarie={
            "character":char,"amount":value
        }
        dictionarie_list.append(dictionarie)
    
    dictionarie_list.sort(reverse=True,key=sort_on)

    return dictionarie_list