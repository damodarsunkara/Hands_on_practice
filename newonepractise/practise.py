#table upto 5 beside  
for i in range(1,11):
    for j in range(1,6):
        print(j,"x",i,"=",j*i,end="\t")
    print()

#list comprehension
li=[[1,2,3],[4,5,6],[8,9,0]]
li=[j for i in li for j in i]
print(li)


#convert into dictonary of two lists
p=["pid","name","age"]
o=[101,"rama",20]
di={k:v for k in p for v in o}
print(di)

#flattend into list of elements

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


num=1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
        num+=1
    print()


#

