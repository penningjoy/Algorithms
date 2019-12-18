''' --------------------------------------------------------  ''                         
Binary Search using Python
Sample set : [6,3,8,1] 
Rule -> 1. Sort the set => 1,3,6,8
        2. Do a search by recursively diving the set in half.
'' ---------------------------------------------------------- '''

def binary_search(list, number):
    length = len(list)
    pivot = list[(length//2) -1]
    
    if(length == 1):
        if(number == pivot):
            return True
        else:
            return False
    else:
        if(number == pivot):
            return True
        elif(number < pivot):
            list = list[:length//2]
            return binary_search(list, number)
        elif(number > pivot):
            list = list[length//2:length]
            return binary_search(list, number)
        else:
            return False

def main():
    numList = list(map(int, input("Enter a multiple values separated by commas: ").split(',')))
    numList.sort()
    number = int(input("Enter a number to search: ")) 
    expection = input("Enter your expectation - Found/Not Found :")
    found = binary_search(numList, number)
    print("The record was found : " , found)
    if(expection.lower() == "found"):
        assert found == True , "The expectation is the number will be found." 
    else:
        assert found == False , "The expectation is the number will not be found."
    


if __name__ == '__main__':
    main()
