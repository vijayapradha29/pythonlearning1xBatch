string=input("Enter a String:\n")
string1=string.lower()
length_of_string=len(string)
count=0
count1=0
for i in string1:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
        vowels=count
    elif i==" ":
        count1+=1
        space=count1
consonants=length_of_string-count-count1
print(consonants)
print(f"The Number of Vowels is:",count,"and","\n","The Number of Consonants is:",consonants)
