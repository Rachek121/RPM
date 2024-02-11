word1 = input().split(",")
order = input()
for i in word1:
    if order.lower().find(i.lower()) != -1:
        print("True")
    else:
        print("False")
    break
