#1
def square(*num):
    i=1
    for i in num:
        i*=i
    return i

li=list(map(square,[1,2,3,4]))
print(li)

#2
li3=list(map(lambda x:x**2,[1,3,4,5,6]))
print(li3)


#3
def even(*num):
    for i in num:
        if i%2==0:
            
            return True
    
        
li4=tuple(filter(even,(1,2,3,4,5,6)))
print(li4)

#4
li5=tuple(filter(lambda x:x%2==0,(1,2,3,4,5)))
print(li5)

#5
x=10
def outer():
     print(x)

outer()

#6
x=12
def outer1():
    x=14
    print(x)
    def inner():
        x=16
        print(x)
    inner()
  
outer1()
#7
x=19
def outer1():
    x=14
    print(x)
    def inner():
        x=16
        print(x)
    inner()
  
outer1()
print(x)

#8
y=10
def outer():
     name="ss"
     global age
     age=21
     def inner1():
          print(f"name is {name} and age is {age}")
     inner1()
outer()
#9
l1=["ss",34,5,6,"ss"]
def ss1():
    for i in l1:
        print(i)
    def ine():
        global l1
        l1=["dd",34]
        for i in l1:
            print(i)
        ine()

ss1()

#10
num=0
def outer11():
    def inner12():
        print("inner")
        num=12
        def inner13():
            print(num)
     
        inner13()
    inner12()
outer11()
    
  

#11
def outer11():
    def inner12():
        print("inner")
        num=12
    inner12()
    def inner13():
       print(num)
     
    inner13()
 
outer11()
#12
if(__name__=="__main__"):
    min1=lambda x,y:x if x>y else y
    print(min1(2,3))
#13
if(__name__=="__main__"):
    mx=lambda x,y,z:x if x>y and x>z else y if y>z else z
    print(mx(1,23,3))

#14
num=[1,2,3,4]
li=lambda :[i for i in num if i%2==0]
print(li())

#15
for i in range(1, 6):
    for j in range(i):
        print(j + 1, end=" ")
    print()


#16
n = 5
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()


#17
def add(a,b):
    print(a+b)
add(3,4)

#18
def add(a,b):
    return a+b
print(add(4,3))
#19
def test():
    return "test"
c=test()
print(c)
#20
def s(n):
    if n%2==0:
        return "even",n
    else:
        return 'odd',n
        
for i in range(20):
    x=s(i)
    print(x)
#21
def ss(*num):
    fa=1
    for i in num:
        fa*=i
    return fa
print(ss(1,2,3,4))


#22
def palindrome(str1):
    for i in str1:
        if i[::-1]==i:
             return i
print(palindrome(["madam","121"]))

#23
def city(num):
    print(num)
    def state():
        print("tg")
    state()
    def country():
        print("india")
    country()
city("hyderabad")
#24
def ss(*n):
    for n in n:
       print( n*n)
  
ss(3,4,5)

#25
names=["damodar","ss"]
names=list(map(lambda x:x.upper(),names))
print(names)
#
name=["Damodar","Ss"]
u=lambda : [i for i in name if i.istitle()]
print(u())

#
i=lambda x:x.istitle()
print(i("Damodaar"))

#
def test(a,b,*c):
    for i in c:
       print(a+b*i)
    
test(2,4,2,3,4)

def test2(name="ss",age="21",game="cricket"):
    print(f"the {name} with {age} is plays{game}")
test2(name="ss2",age="20",game="vollleball")


def test3(name,age="21"):
    return name+" "+ str(age)
    
x=test3("ss",23)
print(x)











    



        



