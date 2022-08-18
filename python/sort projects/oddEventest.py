import unittest

numList = [1,2,3,4,5,6,7,8,9]                               # Initialize the list


def evenOdd(myList: list)-> tuple:                          # Initialize the function
    evens = 0                                               # Stores the number of even nums in the list
    odds = 0                                                # Stores the number of odd nums in the list
    
    for num in myList:                                      # For loop to iterate through the list
        if num % 2 == 0:                                    # If conditional to check for even numbers
            evens += 1                                      # Adds 1 to the even var
        else:
            odds += 1                                       # Adds 1 to the odd var   

    print("Odds: "+str(odds)+", Evens: "+str(evens))        # Prints out the results 
    return (odds,evens)                                     # Returns values in a tuple

#evenOdd(numList)



class Testevens(unittest.TestCase):

    def testevens(self):
        self.assertEqual(evenOdd([1,2,3,7]),(3,1))

    
unittest.main()