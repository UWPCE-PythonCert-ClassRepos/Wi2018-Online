
def func_noError():
    return 'No Error: Done'

def func_valueError():
    try:
        s = "not a number"
        i = int(s.strip())
        print ("will not print this line as it goes to the exception handler")
    except ValueError as e:
        print("Value Error: Exception Message - " + str(e))


def func_typeError():
    try:
        x="one"
        y="two"
        result = x/y
        print ("will not print this line as it goes to the exception handler")
    except TypeError as e:
        print("Type Error: Exception Message - " + str(e))

def func_attributeError():
    try:
        i = 2
        v = i.keys() #this method is not allowed for an integer but only for a Dictionary
        print ("will not print this line as it goes to the exception handler")
    except AttributeError as e:
        print("Attribute Error: Exception Message - " + str(e))
 
#Need to uncomment this method for testing   
#def func_syntaxError():
#    try:
#        for i in (0,5)
#            print (i)
#    except SyntaxError as e:
#        print("Error encountered: ", e)

if __name__ == "__main__":
    func_noError()
    func_valueError()
    func_typeError()
    func_attributeError()
    #func_syntaxError()



