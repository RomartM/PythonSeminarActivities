# Init
original_poem = ("Shall I compare thee to a summer’s day?\n"
"Thou art more lovely and more temperate.\n"
"Rough winds do shake the darling buds of May,\n"
"And summer’s lease hath all too short a date.\n"
"Sometime too hot the eye of heaven shines,\n"
"And often is his gold complexion dimmed;\n"
"And every fair from fair sometime declines,\n"
"By chance, or nature’s changing course, untrimmed;\n")
separator_line = "------------------------------------------------------------"
title_orig = "Original Poem"
title_mod = "Modified Poem"

noun_collection = []
adjective_collection = []


# Input

noun_collection.append(input("Enter 1st noun: "))
noun_collection.append(input("Enter 2nd noun: "))
noun_collection.append(input("Enter 3rd noun: "))

adjective_collection.append(input("Enter 1st adjective: "))
adjective_collection.append(input("Enter 2nd adjective: "))
adjective_collection.append(input("Enter 3rd adjective: "))

# Process

modified_poem = original_poem.replace("summer’s", noun_collection[0].upper(), 1)
modified_poem = modified_poem.replace("shake", noun_collection[1].upper(), 1)
modified_poem = modified_poem.replace("day", noun_collection[2].upper(), 1)

modified_poem = modified_poem.replace("lovely", adjective_collection[0].upper(), 1)
modified_poem = modified_poem.replace("Rough", adjective_collection[1].upper(), 1)
modified_poem = modified_poem.replace("dimmed", adjective_collection[2].upper(), 1)

# Output

print(f"\n{separator_line}")
print(title_orig.upper())
print(separator_line)

print(f"\n{original_poem}")


print(separator_line)
print(title_mod.upper())
print(separator_line)

print(f"\n{modified_poem}")