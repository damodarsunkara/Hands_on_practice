
'''
s="aaaabbbccdd"
t=""
for i in s:
    if i not in t:
        t+=i
        t=t+str(s.count(i))
print(t)
  '''  
'''
u='aaaabbbccdd' 
t=""
i=0
while i <len(u):
    if u[i] not in t:
       t+=u[i]

    count=0
    
    if u[i]==u[i+1]:
        count+=1
    t+=str(count)
    i+=1


print(t)
 '''
def ss(a,b=10):
    return a+b
print(ss(10))
  