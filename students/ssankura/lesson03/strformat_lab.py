
#Task1
def task1(inpt):
	print("***** Task 1 - Printing tuple using format")
	print("file_{:03d} :  {:.2f}, {:.2e}, {:.2e}".format(inpt[0], inpt[1], inpt[2], inpt[3]))

#Task2 - using f-strings
def task2(inpt):
	print("***** Task2 - Printing tuple using f-strings")
	print (f"file_{inpt[0]:03d} :  {inpt[1]:.2f}, {inpt[2]:.2e}, {inpt[3]:.2e}")


#Task3
def task3_formatter(tuple):
	print ("***** Task3 - Printing tuple by dynamically building up format strings")
	form_string = ""
	for i in tuple:
		form_string+= "{:d} "
	print(form_string.format(*tuple))

#Task4
def task4(tuple):
	print ("***** Task4 - printing 5 element tuple")
	print (f"{tuple[3]:02d} {tuple[4]:02d} {tuple[2]:d} {tuple[0]:02d} {tuple[1]:d}")


#Task5
def task5(t):
	print("***** Task5 - Printing tuple using f-strings")
	print (f"The weight of an {t[0][:-1]} is {t[1]} and the weight of a {t[2][:-1]} is {t[3]}")
	print("Printing tuple after converting fruit to Upper case and increasing weight by 20%")
	print (f"The weight of an {t[0][:-1].upper()} is {1.2*t[1]} and the weight of a {t[2][:-1].upper()} is {1.2*t[3]}")

#Task6
def task6(inptList):
	print ("***** Task6 - print Name, Age and Cost using f-strings")
	''' Adding enough spaces to print Column Headers for the table - Name Age and Cost'''
	sp = ' ' * 26
	sp1 = ' ' * 8
	str = "Name" + sp + "  " + "Age" + sp1 + "  " + "Cost"
	print(str)

	for item in inptList:
		print(f"{item[0]:30}  {item[1]:3d}  {item[2]:12}")

#Task6 part2
def task6_part2(t):
	print ("***** Task6 part2 - print Name, Age and Cost using f-strings")
	print (("{:5d}"*len(t)).format(*t))

#Main method which involves all the task methods
def main():
	inpt = (2, 123.4567, 10000, 12345.67)
	task1(inpt)

	task2(inpt)
	
	t = (1,2,3,55,9,21)
	task3_formatter(t)

	t=( 4, 30, 2017, 2, 27)
	task4(t)

	t=(['oranges', 1.3, 'lemons', 1.1])
	task5(t)

	inpt = [("judy",39,1000),("john",8,8900),("mary",11,900),("doug",45,190000)]
	task6(inpt)

	t = (1,2,3,4,5,6,7,8,9,10)
	task6_part2(t)
	
#Invokes the main() method
if __name__ == "__main__":
	main()
