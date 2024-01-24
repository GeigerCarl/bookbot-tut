    
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = word_counter(file_contents)
        print(f"--- Begin report of {f.name} ---")
        print(f"Number of words: {word_count}")
        letter_dict = count_letters(file_contents)
        print(f"Number of letters:\n")
        for character in letter_dict:
            print(f"The '{character}' character was found {letter_dict[character]} times.")


def word_counter(file):
    return len(file.split())

def init_letter_dict():
    letter_dict = dict()
    for ch in "abcdefghijklmnopqrstuvwxyz":
        letter_dict[ch] = 0
    return letter_dict

def count_letters(file):
    letter_dict = init_letter_dict()
    lowercase_file = file.lower()
    for ch in lowercase_file:
        if ch in letter_dict:
            letter_dict[ch] += 1
    return letter_dict

main()