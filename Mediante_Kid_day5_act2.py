
def reverse_string(string):
    reversed_letters = list()
    index = 1

    for letter in string:
        reversed_letters.append(string[ len(string) - index ])
        index += 1

    return "".join(reversed_letters)


word_input = str(input("Input a word: "))
print(f"INPUT: {word_input}")
print("OUTPUT: %s (%d characters)" % (reverse_string(word_input).upper(), len(word_input)))