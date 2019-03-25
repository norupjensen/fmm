#helper functions for math operations performed in mathShowcase and tested in tests.property

"""
goldbach:
any even number larger than 2 can be expressed as the sum of 2 primes:
the flow:
ask for a number
find prime until number
check all prime pairs and return pairing
"""
global primeList

def goldbach():
    getUserInputString = "GoldBach | Enter a number:"
    userInput = input(getUserInputString)
    if (int(userInput) % 2) == 0:
        print("You've choosen {}".format(userInput))
        #basic flow goes here.
        #find prime until user input
        # # check the list to see if we have enough primes in the list
        # else generate more primes!
        # then find pairs

    else:
        print("You entered: " + str(userInput) + " that's not an even number")
    return userInput
