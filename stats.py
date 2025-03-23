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
           