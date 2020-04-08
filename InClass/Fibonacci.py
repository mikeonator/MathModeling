## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree
def main():
    fibList = [1,1]                                                                                                             #List with first two digits of sequence
    #for a in range(0,98):                                                                                                       #for loop from 0-98 because the first two digits are already there
    while(fibList[-1] < 10000):
        fibList.append(fibList[-2] + fibList[-1])                                                                               #Append the sum of the last two digits of the list to the list
    
    print(fibList[-2])                                                                                                          #Print the last number of the sequence less than 10000
    
    #print("\n" + 8*"_" + "\n\n" + "34th: " + str(fibList[34]) + "\n" + "78th: " + str(fibList[77]) + "\n" + 8*"_" + "\n")       #Print 35th and 78th numbers while looking nice

if __name__ == '__main__':                                                                                                      #This thing basically lets the interpreter thing read my code before I run it all the way through because of how Python works
    main()