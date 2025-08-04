def happy(num):
    seen=set()
    cur=str(num)
    while cur not in seen:
        seen.add(cur)
        summ=0
        for digit in cur:
            digit=int(digit)
            summ=summ+digit**2
        if summ==1: return True
        cur=str(summ)
    return False
print(happy(18))





