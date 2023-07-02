def print_rectangle_pattern(word):
    length = len(word)
    horizontal_line = '*' * (length + 6)
    print(horizontal_line)
    for letter in word:
        line = '* ' + letter + ' ' * (length) + ' *'
        print(line)
    print(horizontal_line)
input_word = input("Enter a word: ")
print_rectangle_pattern(input_word)