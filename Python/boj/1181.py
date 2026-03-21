# 1181, 단어정렬, silver 4
#pesudo 
# save 'n' = word number
# repeat n time / 
# save words in list
# sort len(word) & dictionary characters
# 중복제거 use set or deduplicate

n = int(input())
words_set = set()
for i in range(n):
    word = input()
    words_set.add(word) # set doesnt have .append() use .add()

words_set = sorted(words_set,key = lambda x: (len(x), x)) 

for w in words_set:
    print(w)

