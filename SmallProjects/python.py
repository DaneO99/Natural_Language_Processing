#open file
open("TennesseWhiskey.txt",'r')
#print out words
with open("TennesseWhiskey.txt") as f:
    for line in f:
        for word in line.split():
            print(word)
num_words = []
#count number of words
with open("TennesseWhiskey.txt") as f:
    for line in f:
        for word in f:
            num_words.append(word)
print(num_words)
#unique count and word
words = []
with open("TennesseWhiskey.txt") as f:
    for line in f:
        for word in line.split():
            if word not in words:
                words.append(word)
print("Number of unique words:" , len(words))

from collections import Counter
word_counts = Counter()
with open("TennesseWhiskey.txt", 'r') as f:
    for line in f:
        words = line.split()
        word_counts.update(words)

most_common_words = word_counts.most_common(20)
print("The twenty most used words are:")
for word, count in most_common_words:
    print(f"{word}: {count}")