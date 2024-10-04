#file i/o:


# file=open('vijaya.txt','r')
# print(file.read())
# file.close()

#how to write to a file:use append mode

file2=open('vijaya.txt','a')
file2.write("Yes,Yes")
file2.close()

file=open('vijaya.txt','r')
print(file.read())
file.close()