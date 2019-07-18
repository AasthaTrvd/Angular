def avg(*num):
    s=0
    a=0
    for i in num:
        s+=i
        a+=1
    return(s/a)
print(avg(1,2,3,4,5))
print(avg(1,5,6,7,89,10))