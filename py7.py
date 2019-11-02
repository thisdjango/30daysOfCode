n = int(input())
words = [input() for i in range(n)]
for word in words:
    print(word[::2] + ' ' + word[1::2])
