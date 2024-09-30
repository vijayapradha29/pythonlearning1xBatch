#password:
class Password:
    def __init__(self,password):
        self.__password=password
    def set_password(self,password):
        if len(password)>10:
            self.__password=password
        else:
            print("Weak Password")
    def get_password(self):
        return self.__password
    def print_password_length(self):
        print("Your Password Length is:",len(self.__password))

pass_object=Password("123")
pass_object.print_password_length()
new_pass=pass_object.get_password()
print(new_pass)
pass_object.set_password("hello1233236")
pass_object.print_password_length()

