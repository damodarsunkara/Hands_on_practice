for i in range(1, 6):
    for j in range(i):
        print(j + 1, end=" ")
    print()



    n = 5
for i in range(n):
    for j in range(n):
        if  i + j == n - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()

def longest(num):
    seen=set()
    long=""
    count=0
    for i in num:
        if i not in seen:
            seen.add(i)
            long+=i
            count+=1
    print( count,long)
longest("aaabbbabc")

words = ["madam", "hello", "noon", "car", "civic"]
word=list(filter(lambda x:x[::-1]==x,words))
print(word)

people = [("alice", 30), ("bob", 25), ("charlie", 35)]
p=list(map(lambda x,y:x.upper(),y+1),people)
print(p)

