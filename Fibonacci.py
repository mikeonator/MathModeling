## Michael Audi 2020
## Mathematical Modeling - Mr. Sabree

def main():
    fibList = [1,1]                                                                                                             #List with first two digits of sequence
    for a in range(0,98):                                                                                                       #For loop, duh.
        fibList.append(fibList[-2] + fibList[-1])                                                                               #Append the sum of the last two digits of the list to the list

    print("\n" + 8*"_" + "\n\n" + "34th: " + str(fibList[34]) + "\n" + "78th: " + str(fibList[77]) + "\n" + 8*"_" + "\n")       #Print everything looking nice

if __name__ == '__main__':
    main()