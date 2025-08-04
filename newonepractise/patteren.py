for i in range(6):
    for j in range(5):

        if i in {0,4} and j in {0,1,2,3,4,5}:
            print("*",end=" ")
        elif i in {1,2,3,4} and j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()





x=["flowers","flows","follows"]
s=""
i=0
while i<1:
    j=0
    while j<3:
        if x[i][j] == x[i+1][j]== x[i+2][j]:
            print(x[i][j])
            j+=1
        i+=1
        
       
print(s)