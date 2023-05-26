satisfaction = [-1,-4,-5]

satisfaction.sort(reverse=True)

satisfaction = [x for x in satisfaction if x >= 0]
        

print(satisfaction)
total = 0 

for i in range(len(satisfaction)):
    dish = satisfaction[i] * (len(satisfaction)-i)
    total += dish

print(total)