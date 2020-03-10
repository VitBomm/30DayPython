n = int(input())
word_dict = dict()
for i in range(n):
    word = input()
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print(len(word_dict))
print(' '.join(map(str,word_dict.values())))
        
