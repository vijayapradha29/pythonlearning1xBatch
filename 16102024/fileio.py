file=open('new.txt','r')
print(file.read())
file.close()

file1=open('new.txt','a')
file1.write("Bye!Bye!")
file1.close()
file=open('new.txt','r')
print(file.read())
file.close()

file3=open('../15102024/new2.txt','r')
print(file3.read())
file3.close()

file4=open('../15102024/new2.txt','w')
file4.write("tata")
file4.close()

