#exception-file not found error:
from idlelib.browser import file_open

try:
    file=open('vijaya5.txt','r')
    print(file.read())
    # file.close()
except FileNotFoundError as error:
    print("Error:",error)
finally:
    if file_open:
        file.close()