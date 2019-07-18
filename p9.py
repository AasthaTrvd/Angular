l=[]
for i in range(1,50):
     l.append(i)

result = filter(lambda x: x % 2, l) 
print(list(result))