#file handling:
#if file does not exists-ill get filenotfound error and how to handle it

try:
    with open("new.txt",'r') as file:
        content1=file.read()
        print(content1)
except Exception as error:
    print("Error:",error)