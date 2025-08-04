#number divisble by 7 in a range(50)
for i in range(1,51):
    if i%7==0 :
        print(i,"is","divisble by 7")
        

user=int(input("enter the number to check it is both divisble by 3 and 5"))
if user%3==0 or  user%5==0:
    if user%3==0:
        print("divisble by 3")
    else:
        print("not divisbleby 3")
    if user%5==0:
        print("divisble by 5")
    else:
        print("not divisble by 5")