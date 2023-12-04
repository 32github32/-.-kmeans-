data = ['P04637', 'P02340', 'P10361', 'Q29537', 'pe46']
data2= []
for k in data:
    if k not in data2:
        data2.append(k)
print(data2)
#['P04637', 'P02340', 'P10361', 'Q29537', 'pe46']


List = [23, 65, 19, 90]
pos1 = 1
pos2= 3
t=List[pos1]
List[pos1] = List[pos2]
List[pos2]=t
print(List)
#[23, 90, 19, 65]

List = [23, 65, 19, 90]
#pos1 = 1
#pos2= 3
t=List[1] 
List[1] = List[3]    
List[3]=t
print(List)
#[23, 90, 19, 65]




