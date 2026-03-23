list=[0,1,0,3,12]
result=[]
for num in list:
    if num!=0:
        result.append(num)
zero_count=list.count(0)
result+=[0]*zero_count
print(result)