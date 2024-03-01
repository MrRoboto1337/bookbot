def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = count_words(file_contents)
    print(f"number of words: {words}")

    letter_dictionary = count_letters(file_contents)
    # print(f"dictionary: {letter_dictionary}")

    create_report(letter_dictionary)


def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def create_report(unsorted_dict):
    # print(f" unsorted dict: {unsorted_dict.items()}")
    sorted_dict = dict(sorted(unsorted_dict.items(), reverse=True, key=lambda item: item[1]))
    for key, value in sorted_dict.items():
        print(f" The '{key}' character was found {value} times")



main()