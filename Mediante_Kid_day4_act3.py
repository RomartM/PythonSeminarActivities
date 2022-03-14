# Init

want_to_continue = True
list_of_words = list()

# Process

while want_to_continue:
    input_word = str(input("Enter a word: "))
    list_of_words.append(input_word)
    is_continue = str(input("Would you like to try again? [Y/N]")).lower()
    if(is_continue == 'n'):
        print("The total word count is %d and the words are the following:" % (len(list_of_words)))
        index = 1
        for word in list_of_words:
            print(f"{index}. {word}")
            index += 1
        want_to_continue = False
        break;
