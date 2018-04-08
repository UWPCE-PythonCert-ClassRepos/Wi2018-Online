# Step 1
#     Create a new module series.py in the lesson02 folder in your student folder.
#         In it, add a function called fibonacci.
#         The function should have one parameter, n.
#         The function should return the nth value in the fibonacci series.
#     Ensure that your function has a well-formed docstring
# Note that the fibinacci series is naturally recursive – the value is defined by previous values:
# fib(n) = fib(n-2) + fib(n-1)
print("Please, call the function using fib(n), where n is the n'ieth number of the Fibonacci series")
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
print (fib)


# Example with n=4 --> fib(4)
# fib(4)=fib(3) + fib(2)
# fib(3)=fib(2) + fib(1)
# fib(2)=fib(1) + fib(0)
# fib(1)=1
# fib(0)=0
# Going back:
# fib(2)=1+0=1
# fib(3)=1+1=2
# fib(4)=2+1=3
# It worked.
