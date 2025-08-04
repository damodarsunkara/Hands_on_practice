
'''
li=[9,4,3,2]
start=0
end=len(li)
for i in range(0,end-1):
    li[start],li[i+1]=li[i+1],li[start]
    start+=1
if start>0:
    start=0
for i in range(0,end-2):
    li[start],li[i+1]=li[i+1],li[start]
    start+=1
if start>0:
    start=0
for i in range(0,end-2):
    li[start],li[i+1]=li[i+1],li[start]
    start+=1


print(li)
'''

li=[1,2,35,6,7]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        li[i],li[j]=li[j],li[i]

print(li)



