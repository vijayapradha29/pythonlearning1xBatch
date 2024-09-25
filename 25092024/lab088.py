words=["apple","banana","cherry","date","elderberry","fig"]
min_len=6
length=len(words)
print(length)

# def min_words(words):
#     if length==min_len:
#         print("length is 6")
#     else:
#         print("length is not 6")
# min_words(words)

def min_words(words):
    return len(words)>min_len
# print(min_words(words[0]))
#or
output=list(filter(min_words,words))
print(output)