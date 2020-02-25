minusOne = 1
minusTwo = 1
print(str(minusOne) + "\n" + str(minusTwo))
for a in range(0,50):
    curNum = minusOne + minusTwo
    print(curNum)
    minusTwo = minusOne
    minusOne = curNum
    
