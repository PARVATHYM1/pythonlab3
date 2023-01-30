input = "word.txt"
longest_word = ""
with open(input) as f:
    for word in f:
        if len(word) > len(longest_word):
            longest_word = word
            
print(longest_word)
