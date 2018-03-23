
def exchangeFirstLast(seq):    
    """
    The return sequence of slice values 
    exchanges the last element with the last element
    and vice versa
    """    
    a_new_seq = seq[:]    
   
    return a_new_seq[-1:] + a_new_seq[1:-1] + a_new_seq[:1]

def everyOtherItem(seq):
    """
    The two colons without specified parameter will include all the characters from the original string, 
    a stride of 2 will include every other character.
    """
    a_new_seq = seq[:]
        
    return a_new_seq[::2] 

def firstLast4Items(seq):
    """
    Slicing the sequence removes the first & last four elements, then steps every other item
    """
    a_new_seq = seq[:]
    
    return a_new_seq[4:-4:2]

def itemsReversed(seq):
    """
    Omitting the two index numbers and retaining colons will keep the whole string within range, 
    while adding a final parameter for step will specify the number of characters to skip.
    Additionally, you can indicate a negative numeric value for the stride, 
    which we can use to print the original string in reverse order if we set the stride to -1
    """
    a_new_seq = seq[:]
    
    return a_new_seq[::-1]

def returnByThrids(seq):
    """
    This format follows the format of the function exchange the first and last elements vaules 
    except it is divided by thirds. The // is floor division which essentially rounds down the divsors
    """
    a_new_seq = seq[:]
    thirds = len(a_new_seq) // 3
    return a_new_seq[thirds:-thirds] + a_new_seq[-thirds:] + a_new_seq[:thirds]

def main():
    tst_string = "Python slicing is wicked awesome"
    tst_tuple = (0,1,2,3,4,5,6,7,8,9,10)

    print('-'*90)
    print("Exchanging first & last element for string: {}".format(tst_string), end='\n')
    print("Returns: " + exchangeFirstLast(tst_string),end='\n')
    assert exchangeFirstLast(tst_string) == "eython slicing is wicked awesomP"

    print("Exchanging first & last element for tuple: {}".format(tst_tuple), end='\n')
    print("Returns: "+ str(exchangeFirstLast(tst_tuple)),end='\n')
    assert exchangeFirstLast(tst_tuple) == (10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    print('-'*90)
    print("Printing every other item for string: {}".format(tst_string), end='\n')
    print("Returns: " + everyOtherItem(tst_string),end='\n')
    assert everyOtherItem(tst_string) == "Pto lcn swce wsm"

    print("Printing every other item for tuple: {}".format(tst_tuple), end='\n')
    print("Returns: " + str(everyOtherItem(tst_tuple)),end='\n')
    assert everyOtherItem(tst_tuple) == (0, 2, 4, 6, 8, 10)

    print('-'*90)
    print("Printing removed first and last four items, and every other in between for string: {}".format(tst_string), end='\n')
    print("Returns: " + firstLast4Items(tst_string),end='\n')
    assert firstLast4Items(tst_string) == "o lcn swce w"

    print("Printing removed first and last four items, and every other in between for tuple: {}".format(tst_tuple), end='\n')
    print("Returns: " + str(firstLast4Items(tst_tuple)),end='\n')
    assert firstLast4Items(tst_tuple) == (4, 6)

    print('-'*90)
    print("Printing items in reverse order for string: {}".format(tst_string), end='\n')
    print("Returns: " + itemsReversed(tst_string),end='\n')
    assert itemsReversed(tst_string) == "emosewa dekciw si gnicils nohtyP"

    print("Printing items in reverse order for tuple: {}".format(tst_tuple), end='\n')
    print("Returns: " + str(itemsReversed(tst_tuple)), end='\n')
    assert itemsReversed(tst_tuple) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

    print('-'*90)
    print("Printing middle third, last third, then first third for string: {}".format(tst_string), end='\n')
    print("Returns: " + returnByThrids(tst_string),end='\n')
    assert returnByThrids(tst_string) == "cing is wicked awesomePython sli"

    print("Printing middle third, last third, then first third for tuple: {}".format(tst_tuple), end='\n')
    print("Returns: " + str(returnByThrids(tst_tuple)))
    assert returnByThrids(tst_tuple) == (3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2)

if __name__ == "__main__":
    main()