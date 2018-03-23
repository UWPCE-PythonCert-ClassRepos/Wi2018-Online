#!/usr/bin/env python3

def task_one():
    t1 = (2, 123.4567, 10000, 12345.67)
    str1 = '{:03d}'.format(t1[0])
    str2 = '{:.2f}'.format(t1[1])
    str3 = "{:.2E}".format(t1[2])
    str4 = "{:.2E}".format(t1[3])
    print ('file_'+str1+': '+str2 + ', ' + str3 + ', ' + str4)

def task_three(nums):
    string_format = '{:d}'*3
    test = ','.join(string_format)
    print (test)
    print ("the {:d} numbers are: {:d}, {:d}, {:d}".format(len(nums),*nums))

def task_four(nums):
    print (nums)
    print ("{:02d}, {:d}, {:d}, {:02d}, {:d}".format(nums[3],nums[4],nums[2],nums[0],nums[1]))

def task_five():
    f_string = ['oranges', 1.3, 'lemons', 1.1]
    print ("The weight of an {} is {:.1f} and the weight of a {} is {:.1f}".format(f_string[0], f_string[1],f_string[2],f_string[3]))

def task_six():
    print("{:20}{:10}{:20}{:8}".format('First', '$99.01', 'Second', '$88.09'))

def main():
    try:
        task_one()
    except:
        print ('error with task 1')
    try:
        nums = (34, 56,77)
        task_three(nums)
    except:
        print ('error with task 3')
    try:
        tup = (4, 30, 2017, 2, 27)
        task_four(tup)
    except:
        print ('error with task 4')
    try:
        task_five()
    except:
        print ('error with task 5')
    try:
        task_six()
    except:
        print ('error with task 6')

if __name__ == "__main__":
    main()