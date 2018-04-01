# Task 1
print("\nTask 1")
tuple1 = (2, 123.4567, 10000, 12345.67)

file_num = tuple1[0]
if file_num >= 10:
	file_name = "file0" + str(file_num)
else:
	file_name = "file00" + str(file_num)

print("{}: {:.2f}, {:.2E}, {:.3E}".format(file_name,tuple1[1],tuple1[2],tuple1[3]))


# Task 2
print("\nTask 2")
print(f"{file_name}: {tuple1[1]:.2f}, {tuple1[2]:.2E}, {tuple1[3]:.3E}")

	
print("\nTask 3: call formeter(tuple)")
def formater(tuple_in):
    num_q = len(tuple_in)
    num_list = ""								# initialize num_list as a str
    for index in range(num_q):					# feed the numbers to a single str
        num_list += str(tuple_in[index])
        if index+1 < num_q:						# index + 1 look ahead that the last counter is indeed the last one
            num_list += ", "					# not the last number, add a comma
    print(f"the {num_q} numbers are: " + "{}".format(*tuple_in)	*len(tuple_in))

	
# Task 4
print("\nTask 4")
tuple4 = (4, 30, 2017, 2, 27)
print(tuple4)
print("{3:02d} {4} {2} {0:02d} {1}".format(*tuple4))

# Task 5
print("\nTask 5")
tuple5 = ("oranges", 1.3, "lemons", 1.1)
print(tuple5)
name1 = tuple5[0]
name2 = tuple5[2]
print(f"The weight of an {name1[:-1]} is {tuple5[1]} and the weight of a {name2[:-1]} is {tuple5[3]}")
print(f"The weight of an {name1[:-1].upper()} is {tuple5[1]*1.2} and the weight of a {name2[:-1].upper()} is {tuple5[3]*1.2}")

# Task 6
print("\nTask 6")
l6_names = ["Vik", "Dan", "Steve", "Alexander"]
l6_ages = [18, 20, 14, 32, 120]
l6_owes = [0, -250.23, 50.55, 70]
print("{:15}|{:^5}|{:>10}".format("Names","Age","Owes [$]"))
print("_"*(15+5+10))
for index in range(int(len(l6_names))):
    print("{:15}|{:^5}|{:>10.2f}".format(l6_names[index],l6_ages[index],l6_owes[index]))

print()
t6_nums = (1,2,3,4,5,6,7,8,9,10)
print(t6_nums)
print(("{:^5}"*10).format(*t6_nums))
