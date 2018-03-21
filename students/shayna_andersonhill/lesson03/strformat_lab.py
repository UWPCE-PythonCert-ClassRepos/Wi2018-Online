#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
#Shayna Anderson-Hill
#Goal: Learn string formatting
#03-03-2018

#Task One
to_format = (2, 123.4567, 10000, 12345.67)

print(f"file_{to_format[0]:03} :   {to_format[1]:.2f}, {to_format[2]:.2e}, {to_format[3]:.2e}")

#Task Two
print("file_{:03} :   {:.2f}, {:.2e}, {:.2e}".format(to_format[0], to_format[1], to_format[2], to_format[3]))

#Task Three
def formatter(t):
    placeholders = [" {:d}"]*len(t)
    placeholders = ','.join(placeholders)
    print(f"the {len(t)} numbers are:{placeholders}".format(*t))

formatter((2,3,5))
formatter((2,3,5,7,9))

#Task Four
to_format = ( 4, 30, 2017, 2, 27)
print(f"{to_format[3]:02} {to_format[4]:02} {to_format[2]} {to_format[0]:02} {to_format[1]:02}")

#Task Five
to_format = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {to_format[0][:-1]} is {to_format[1]} and the weight of a {to_format[2][:-1]} is {to_format[3]}")

print(f"The weight of an {to_format[0][:-1].upper()} is {to_format[1]*1.2} and the weight of a {to_format[2][:-1].upper()} is {to_format[3]*1.2}")

#Task Six
data = [('Shayna', '29', '$444.58'), ('Brandon', '30', '$10000000.00'),
        ('Leonardo', '63', '$1.00')]

for record in data:
    print('{:20}{:10}{:>20}'.format(*record))

consecutive_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(('{:5}'*len(consecutive_numbers)).format(*consecutive_numbers))
