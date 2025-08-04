# power of a number
base=int(input("enter the base"))
exponent=int(input("enter exponent"))
result=1
while exponent>0:
    result*=base
    exponent-=1
    
print(f"power of a number{result}")
#
num=10
while num!=0:
    if num%2==0:
        print("even",num)
    num-=1
#
num1=123
n=0
while num1<=0:
    digit=num1%10
    n+=n*10+digit
    num1=num1//10
print(n,num1)
#
st="madam"
s=""
l=0
while l<len(st):
    s=st[l]+s
    l+=1
print(st==s)
#
fact=int(input("enter the number"))
fa=1
i=1
while i<=fact:
    fa*=i
    i+=1
print(f"{fact} is {fa}")

#reverse
num=10
while num!=0:
    print(num)
    num-=1
else:
    print("number reached ")

#
num3="123"
i=0
while i<len(num3):
    print(num3[i],end=" ")
    i+=1

#
''' empty output
text=""
while text!="r":
    text="s"
'''
#
i=1
while i<=10:
    print(10*i)
    i+=1

#sum of digits 
nn=123
nn1=0
while num!=0:
    digit=nn%10
    nn1+=digit
    nn=nn//10
print(nn1)





