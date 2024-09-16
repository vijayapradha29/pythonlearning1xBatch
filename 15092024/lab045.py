#continue:
# for i in range(1,10):
#     # print(i)
#     if i%2==0:
#         print("Found Even Number")
#         continue
#     else:
#         print(i)

for num in range(1,5):
    if num%2==0:
        print(f"Found Even Number {num}")
        continue
    print(f"Found Odd Number {num}")