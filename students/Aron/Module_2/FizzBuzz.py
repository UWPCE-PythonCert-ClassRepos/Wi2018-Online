# generate the results table
result_table =[ (i, not i%3, not i%5) for i in range(1,100) ]

# convert table values to a string
message = {
    (True,True):'FizzBuzz',
    (True,False):'Fizz',
    (False,True):'Buzz',
    (False,False):''
}

# we build the results list by passing the truth table through the message dictionary
# i is chosen if message[(p,q)] == ''
results = [ message[(p,q)] or i for (i, p, q) in result_table ]

# print the results
for result in results:
    print(result)

if __name__=="__main__":
    print('This is run as module')
