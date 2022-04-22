
def main():

    word_to_compute = {}
    text = input("Text: ")
    words = text.split()

    convert_to_dict(word_to_compute, words)

    words = list(word_to_compute.keys())
    words.sort()
    longest_word = max((len(word)) for word in words)

    print_word_occur(word_to_compute, longest_word, words)


def convert_to_dict(WORD_TO_COMPUTE, words):
    for word in words:
        number_of_word = WORD_TO_COMPUTE.get(word, 0)
        WORD_TO_COMPUTE[word] = number_of_word + 1


def print_word_occur(WORD_TO_COMPUTE, longest_word, words):
    for word in words:
        print(f"{word:{longest_word}} = {WORD_TO_COMPUTE[word]}")

if __name__ == '__main__':
    main()