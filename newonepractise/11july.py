x=[1,2,3,4]
start=0
end=len(x)-1

for i in range(end):
    x[start],x[end]=x[end],x[start]
    start+=1
    end-=1
   
print(x)


p=[4,1,3,5]
for i in range(len(p)):
    for j in range(1,i+1):
        ss=p[i]
        p[i]=p[j]
        p[j]=ss
print(p)

l=[1,2,3,4,1,4,5,2,1,1]
k=[]
for i in l:
    if l.count(i)>1:
       k.append(i)
   
print(k)


p=[[1,2,3,[9,3,7],7,3],"abc","a","b"]
e=[]
for i in p:
    if isinstance(i,list):
        for j in i:
            if isinstance(j,list):
                for u in j:
                    e.append(u)
            else:
                e.append(j)
            
    else:
        e.append(i)
print(e)



   


