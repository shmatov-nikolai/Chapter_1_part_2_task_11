# Given a string consisting of words separated by spaces. Determine how many
# words it has. To solve the problem, use the method count.

string = "Given a string consisting of words separated by spaces. Determine how many words it has."
words = []
words = string.split(' ')
unique_word = ()
unique_word = set(words)
print(f"строка состоит из: {len(unique_word)} уникальных слов")
print (unique_word)
