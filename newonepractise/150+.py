user="ss"
if user:
    print("welcome")
#2
y=0
a=6
b=9
if a==0:
    b+=1
else:
    a+=1
print(a)
#3
if y<=0:
    if a>0:
        y+=4
    else:
        print("ivalid")
else:
    print("invalid")

#4
t=["d","j","0","k","o"]
for i in t:
    if i=="d":
        pass
    print(i,end=" ")
#5
count=1
while count>0:
    print("five times")
    if count==5:
        break
    count+=1 
#6
coun=0
while coun<3:
    print(coun)
    if coun==2:
        break
    coun+=1
#
coun=6
while coun>2:
    print("coun")
    if coun==7:
        break
    coun+=1
else:
    print("out of the box")

#7
num=0
for i in range(10):
    if i%2==0:
        num+=1
print(num)
#8
num=0
for i in range(10):
    if i%2!=0:
        num+=1
print(num)
#9
num=0
for i in range(10):
    if i%2==0:
        num+=1
    else:
        num-=1
print(num)
#10
for i in range(4):
    print(i*"#",end=" ")
print()
#11
i=10
while i>0:
    if i==8:
        continue
    print(i)
    i-=1
else:
    print("skips ")
print()
#12
j=3
while j>0:
    print(j*"7",end="")
    j-=1
else:
    print("out")

#13

for i in range(6):
    e=int(input("enter the number"))
    print(e)

#14
li=["name","age",'collge']
li1=["ss",21,"ss"] 
di={k:v for k in li for v in li1}
print(di)

#15
a="tomato"
di2={a:a.count(i) for i in a}
print(di2)

#16
#list comprehension
li=[ i*i for i in range(10)]
print(li)
#17
li1=[i*i for i in range(11) if i%2==0]
print(li1)
#18
li2=[ i*i for i in range(11) if i%2!=0]
print(li2)
#19
li=[ i*i for i in range(11) if i%2==4]
print(li)
#20
dic={ i:i**2+3 for i in range(11) if i%2==0}
print(dic)
print(type(dic))
for i,k in dic.items():
    print(i,":",k)
se={i for i in range(11) if i%2==0}
print(se)
print(type(se))
#21
s="interviewready"
l=[i for i in s if i in "aeiouAEIOU"]
print(l)
#22
nums=[1,2,3,4,5,6]
nums=[i+4 for i in nums if i%2==0]
print(nums)
#23
num=[3,-1,5,-7,0]
num=[i for i in num   if i<0 ]
print(num)
#24
num=[2,4,5,7]
usr=int(input("enter the number"))
if usr in num:
    print("u guessed it ")
    usr=input("yes guess another")
    if usr not in num:
        print("number is not there")
print("tyr again")
#25
metro_ticket=2
if metro_ticket==2:
    print("entered station")
    metro_ticket-=1
    if metro_ticket==1:
        print("second stationo")
        metro_ticket-=1
        if metro_ticket==0:
            print('out of balance')
print("thank you ")
#26
if user:
    number=input("enter your number to to verify")
    if number[0:2]=="91" and len(number)=="13":
        print("here is your otp is 1234")
        otp=int(input("enter the otp"))
        if otp==1234:
            print("you have successfully created")
print("thank you")
#27

user=input("enter your user name")
pwd=int(input("enter the pwd"))
if user=="user":
    print("welcome",user)
    if pwd==1234:
        print('u successfully login')
print("it will execute re2spective of abobe conditions")
#28
lit=[19,3,4]
li=[]
for i in range(max(lit)):
    if i not in lit:
        li.append(i)
print(li)
#29
u=10
while u>0:
    print(u)
    if u==5:
        break
    u-=1

#30
for i in range(10):
    if i!=0:
        print("odd numbers")
#31
# 
base=int(input("enter the base"))
exponent=int(input("enter exponent"))
result=1
while exponent>0:
    result*=base
    exponent-=1
    
print(f"power of a number{result}")
#32
num=10
while num!=0:
    if num%2==0:
        print("even",num)
    num-=1
#33
num1=123
n=0
while num1<=0:
    digit=num1%10
    n+=n*10+digit
    num1=num1//10
print(n,num1)
#34
st="madam"
s=""
l=0
while l<len(st):
    s=st[l]+s
    l+=1
print(st==s)
#35
x=[1,2,9,5,2]
o=[]
y=1
t=max(x)


while y<=9:
    if y not in x:
        o.append(y)
    y+=1
print(o)
#36
num=20
l=0
while l<=4:
    j=0
    while j<4:
        print(num,end=" ")
        num-=1
        j+=1
    print()
    l+=1
    

#37
fact=int(input("enter the number"))
fa=1
i=1
while i<=fact:
    fa*=i
    i+=1
print(f"{fact} is {fa}")

#38
num=10
while num!=0:
    print(num)
    num-=1
else:
    print("number reached ")

#39
num3="123"
i=0
while i<len(num3):
    print(num3[i],end=" ")
    i+=1

#40

text=""
while text!="r":
    text="s"

#41
i=1
while i<=10:
    print(10*i)
    i+=1

#42 
nn=123
nn1=0
while num!=0:
    digit=nn%10
    nn1+=digit
    nn=nn//10
print(nn1)
#43
user=input("m pin number")
if user!="1234":
    
        print("incorrect mpin")
        user=input("enter the mpin again")
        if user=="1234":
            number=input("enter the number to send otp to verify")
            if number.startswith("91") and len(number) ==13:
                print("your otp is 3456")
                otp=int(input("your otp"))
                if otp!=3456:
                    print("incorrect otp")
                    otp=input("enter the otp again")
                    if otp==3456:
                         print("you login successfully")
                    else:
                        print("you have successfully login")
                elif otp==3456:
                         print("you login successfully")
       
            else:
                print("ensure u number start with 91 and length of the number is 13")
                number=input("enter the number to send otp to verify")
                if number.startswith("91") and len(number) ==13:
                    print("your otp is 3456")
                    otp=int(input("your otp"))
                    if otp==3456:
                        print("you have successfully login")
                        
                    else:
                        print("incorrect otp")
                        otp=input("enter the otp again")
                        if otp==3456:
                            print("you login successfully")

else:
     
            number=input("enter the number to send otp to verify")
            if number.startswith("91") and len(number) ==13:
                print("your otp is 3456")
                otp=int(input("your otp"))
                if otp==3456:
                     print("you have successfully login")
                
                else:
                    print("incorrect otp")
                    otp=int(input("enter the otp again"))
                    if otp==3456 and len(str(otp))==4:
                       print("you login successfully")    
                    
                

            else:
                print("ensure u number start with 91 and length of the number is 13")
                number=input("enter the number to send otp to verify")
                if number.startswith("91") and len(number) ==13:
                    print("your otp is 3456")
                    otp=int(input("your otp"))
                    if otp!=3456  and len(str(otp))==4:
                         
                         pass
                    else:
                        print("incorrect otp")
                        otp=int(input("enter the otp again"))
                        if otp==3456 and len(str(otp))==4:
                            print("you login successfully")    

#
li=[3,4,5,6,7]
l=[]
a1=0
while a1<(len(li)):
    if li[a1]%2==0:
        l.append(li[a1])
        a1+=1
print()
#
e="this is the code".replace(" ","")
t={i:e.count(i) for i in e}
print(t)

#
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

#
for i in range(1,51):
    if i%7==0 :
        print(i,"is","divisble by 7")

#
l=[[3,4,5],[2,3],9,10]
li1=[]
for q in l:
    if type(q)==list:
        for j in q:
           li1.append(j)
    else:
        li1.append(q)
print(li1)
#
x=[["a","A","B"],["d","r","l"],["v","v"]]
for i in x:
    for j in i:
        print(j)
print()
#
for i in x:
    for j in i:
        print(j,end="\t")
    print()

#
for i in range(5):
    for j in range(1,10):
        if j%2==0:
           print(j,end="  ")
    print()

#
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
        num+=1
    print()

#
num=1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()
ds=1
for i in range(5):
    for j in range(i+1):
        print(ds,end=" ")
        ds+=1
    ds-=1
    print()

ss=20
for i in range(5):
    print(i,end=" ")
    for j in range(4):
        print(end="")
        print(ss,end='   ')
        ss-=1
    print()
                   
r=[["d","b","b"],["f","r","t"],["r","y","u"]]
i=0
while i<len(r):
    print(r[i])
    j=0
    while j<len(r[i]):
        print(r[i][j])
        j+=1
    i+=1
    print()    

y=["ss@gail.com","rr@gmail.com","rrg.com"]
for i in y:
    if i[-10:]=="@gmail.com":
        print(i)
    


y=["ss@gail.com","rr@gmail.com","rrg.com"]
for i in y:
    if i.endswith('@gmail.com'):
        print(i)
    else:
        print("no valid email")

    
student=int(input("enter how many subjects do you have\n"))
marks=0

for i in range(student):
    student=int(input("enter the marks subject wise  "))
    marks+=student
percentage=marks/500*100
if percentage > 96 and percentage<=100:
    print("you have grade A+")
elif percentage>90 and percentage<=95:
    print("you got grade A")
elif percentage>85 and percentage<=90:
    print("you got grade B+")
elif percentage>80 and percentage<=85:
    print("you got grade B")
elif percentage>75 and percentage<=80:
    print("you got grade C+")
elif percentage>70 and percentage<=75:
    print("you got grade C")
elif percentage >65 and percentage<=70:
    print("you got grade D+")
elif percentage >60 and percentage <=65:
    print("you got grade D")
elif percentage >55 and percentage<=60:
    print("you got grade E+")
elif percentage >50 and percentage<=55:
    print("you got grade E")
else:
    print("you got I")


dic1={1:1,2:3,4:4}
k=1
v=2

if (k,v) in dic1.items():
    print(k,v)





k=[]
for i in l:
    if l.count(i)>1:
       k.append(i)
   
print(k)
            

for i in range(5):
    for j in range(5):
       if i in {0,4} and j in {0,4}:
           print("8",end=" ")
       elif i==1 and j in {0,1,3,4}:
           print("8",end=" ")
       elif i==2 and j in {0,2,4}:
           print("8",end=" ")
       elif i==3 and j in {0,1,3,4}:
           print("8",end=' ')
      
       
       else:
           print(" ",end=" ")
    print()       


#
r="damodar"
y="damodar"
if r==y:
    print("matches")
#
t=input("enter the string")
if t.isupper():
    print("uppercase")
else:
    print("not in uppercase")

#
print("welcome to boating")
user=int(input('enter the age to check ticket price'))
if user>8:
    print("100")
elif user>=8 and user<=15:
    print("150")
elif user>=16 and user<=20:
    print("250")
else:
    print("300")

#
user1=input("enter the month i will tell seasoon")
if user1 in ["december","january","feburary"]:
    print("winter")
elif user in ["march","april","may","june"]:
    print("summer")

else:
    print("monsoon")


#
user=int(input("enter the year to know leap year"))
if user//4==0 and user//4000:
    print("leap year")
else:
    print("not a leap year")

#
e=input("enter the country to knnow")
if e == "india":
    print("22 languages")
elif e =="asia ":
    print("english")
else:
    print("english")

#
row=5
for i in range(row):
    print(""*(row-i),end="")
    for j in range(i+1):

        print("* ",end="")


#
for i in range(5):
    for j in range(i+1):
        print("8")
#
s="control statements"
for i in range(len(s),0,-1):
    print(s[i])

#
num=20
for i in range(5):
    for j in range(5):
        print(num,end=" ")
        num-=1
#
s="aiodkflkdeprof"
s1=""
for i in s:
    if i not in "aeiou":
        s1+=i

#
def ss(num):
    num1=num
    reverse=0
    while num!=0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse==num1
for i in range(100,120):
    print(ss(i))

#
s="ascii characters"

for i in s:
    print(i,"--",ord(i))

#
s="noof words"
count=0
for i in s:
    count+=1
print(count)

#
u="sdf  "
if u.isspace():
    print("having space")
#
i=3
num=4
u=int(input("enter the name"))
while i<0:

    if u==num:
        print("you guessed the number")
        break
    else:
        i-=1
        print("try again you have",i)
    

#
summ=0
i=1
while i>0:
    summ+=i
    if summ==100:
        break
    i+=1
#:
for i in range(10):
    for j in range(10):
        if i%2==0 and j%2==0:
            print((i,j),end=' ') 

#
user=input("enter the user pwd")
pin=int(input("enter the pin"))
if user=="1234":
    if pin!=12222:
        print("mistmatch pin with this user")
    else:
        print("you have successfully login")
else:
    print("invalid user")

#
vs=[]
for i in range(10):
    for j in range(10):
        if i+j==10:
            if i and j not in s:
                s.append(i)
                s.append(j)
                print((i,j))

u=int(input("enter the number"))
l=[]
for i in range(1,11):
    l.append(i)

for i in range(u,1,-1):
    if i in l:
        l.remove(i)
        print(i)
for i in l:
    print(i)



num=145
num1=num
strong=0
while num!=0:
    digit=num%10
    fa=1
    for i in range(1,digit+1):
        fa*=i
    strong=strong+fa
    fa=1
    num=num//10
print(strong==num1)
#
otp=input("enter the otp")
while otp=="1234":
    otp=input("enter the otp")
else:
    print("invalid")


ll=[["a","b",'c'],["d","e","f"],["g","i","j"]]
i=0
while i<len(ll):
   
    j=0
    while j<len(ll[i]):
        print(ll[i][j],end=" ")
        j+=1
   
   
    i+=1

ll=[["a","b",'c'],["d","e","f"],["g","i","j"]]
i=0
while i<len(ll):
    print(li[i])
    j=0
    while j<len(ll[i]):
        print(ll[i][j])
        j+=1
    i+=1


ll=[["a","b",'c'],["d","e","f"],["g","i","j"]]
for i in ll:
     for j in i:
         print(j,end=" ")


ll=[["a",20,'c'],["d",100,"f"],["g","90","j"]]
i=0
while i<len(ll):
    print(ll[i])
    j=0
    while j<len(ll[i]):
        print(j,end=" ")
        j+=1
    print()

    i+=1



num=71
for i in range(2,71):
    if num%i==0:
        print("not a prime")
         
     
    else:
        print("prime",num)
        break

s="thoma"
t="homat"
if sorted(s)==sorted(t):
    print("anagram")
else:
    print("not a anagram")


t=["thomas","listen"]
s=["mastho","lients"]
for i in t:
    for j in s:
        if sorted(i)==sorted(j):
            print(i,"anagram")


row=5
for i in range(row):
    print(""*(row-1),end=" ")
    for j in range(i+1):
        print("* ",end=" ")
        
    print()


row=5
for i in range(row):
    print(" "*(row-i),end=" ")
    for j in range(i+1):
        print("*    ",end=" ")
        
    print()


row=5
for i in range(row):
    print(" "*(row-i),end=" ")
    for j in range(i+1):
        print("* ",end=" ")
        
    print()
       
if True:
    print("it will run") 


if False:
    print("it will not")
else:
    print("it will not print")

 

for i in range(10):
    if i%2==0 and i%3==0:
        print("divids by 2 and 3")
    else:
        print("no number")



if True and True:
    print("it will print")


if "a" not in "niml":
    print("yes not in")


names=["alice","bob"]
for i in names:
    print(f'hello {i}')


x=1
while x<100:
    x*=2
    print(x)


i=0
while i<5:
    if i==4:
        print(f"found {i}")
        break
    i+=1


s="damodar"
for i in s:
    print(i.upper())

s="damodar"
for i in s:
    print(i.upper(),end="")


for i in range(1,11):
    if i%3==0:
        print(f"multiples of 3 is {i}")


i=0
while i<10:
    if i==7:
        print("found")
    print(i)
    i+=1

for i in range(19):
    pass


for i in range(1,100):
    if i%2==1:
        continue
    print(f"even number {i}")
    



n=1
while n<19:
    print(n)
    if n==5:
        break
  

for i in range(10):
    print("try",i)
else:
    print("loop finished")


for row in range(3):
    for col in range(3):
        if row == col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#

for i in range(5):
    print("8 ", *(i+1))

for j in range(5,0,-1):
    print("8 "*j)



for i in "hello":
    if i=="l":
        continue
    print(i)


n=7
if n>5:
    if n<10:
        print("between 5 and 10")


n=5
if n>0:
    if n<10:
        if i%2==0:
            print("even")


a,b=6,10
if a<b:
    print("less")


if True:
    if False:
        print("it will print")
    else:
        print("it will print")


if type(5)==int:
    print("yes")



for i in range(1,4):
    print("outerloop",i)
    for j in range(1,3):
        print("inner loop",j)


for i in range(4):
    for j in range(7):
        if i==j:
            print("matches",i,j)


x=15
if x%3==0:
    if x%5==0:
        print("divid by both numbers")


if 5:
    print("holds value")












    



    

        
















      










   


    









     











               










