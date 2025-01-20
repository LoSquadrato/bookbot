def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = get_sorted_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print ()

    for char_dict in sorted_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")

def sort_on(dict):
    return dict["num"]

def get_sorted_list(chars_dict):
    chars_list = []
    for char, num in chars_dict.items():
        char_dict = {"char": char, "num": num}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()