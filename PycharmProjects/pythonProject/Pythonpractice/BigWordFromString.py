string = "python is neweeee"
words = string.split()

# Without key=len, max() would compare alphabetically
longest_word = max(words, key=len)

print("Without key=len, the result is:", longest_word)
