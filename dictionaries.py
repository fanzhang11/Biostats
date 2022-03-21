string = input()

word_count = {}

for word in string.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key in word_count:
    print(key, word_count[key])
