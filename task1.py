import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList

belowFive=[i for i in ourList if i<5]
print(belowFive)
