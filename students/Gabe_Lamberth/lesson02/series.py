# Create Fibonacci Function
def fibonacci(num):
    if (num < 0):
        print("Incorrect input")
        # First Fibonacci number is 0
    elif (num == 0):
        return 0
        # Second Fibonacci number is 1
    elif (num == 1):
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)
    
def lucas_nums(num):
    if (num == 0):
        return 2
    elif (num == 1):
        return 1
    else:
        return lucas_nums(num - 2) + lucas_nums(num - 1)
    
def sum_series(reqNum, opt1 = 0, opt2 = 1):
    # The optional parameters allow for the use of invoking either
    # A Fibonacci Series or a Lucas Numbering series.
    # A 2 in the opt1 parameter is what really sets the Lucas number series
    if (reqNum == 0):
        return opt1
    elif (reqNum == 1):
        return opt2
    else:
        return sum_series(reqNum - 2, opt1, opt2) + sum_series(reqNum - 1, opt1, opt2)
    
def main():
    
    # Test Fibonacci Series with a max range of 9
    print("Printing Fibonacci Series with range of 9")
    for i in range(9):
        print(fibonacci(i), end=',')
        
    # Test Lucas Number Series with max range of 9
    print()
    print("Printing Lucas Number Series with range of 9")
    for i in range(9):
        print(lucas_nums(i), end=',')
        
    print()
    print("Demonstrating Sum Series with no optional parameters")
    # Call Sum Series with no optional parameters
    # This will default to Fibonacci Series
    
    for i in range(9):
        print(sum_series(i), end=',')
        
    print()
    print("Demonstrate Sum Series w/opt1=0 & opt2 =1. Should produce Fibonacci series")
    
    for i in range(9):
        print(sum_series(i, opt1=0, opt2=1), end=',')
    
    print()
    print("Demonstrate Sum Series w/opt1=2 & opt2 =1. Should produce Lucas Number series")  
    for i in range(9):
        print(sum_series(i, opt1=2, opt2=1), end=',')    
        
if __name__ == "__main__":
    main()