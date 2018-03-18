#!/usr/bin/env python3
"""String Formatting Lesson 3 task1"""
file_data = ( 2, 123.4567, 10000, 12345.67)
file_string = 'file_{} :   {}, {}, {}'
file_n = '{0:0{width}}'.format(file_data[0], width=3)
round2 = round(file_data[1],2)
sci_d2 = '{:.2E}'.format(file_data[2])
flt_sci3 = '{:.2E}'.format(float(file_data[3]))
new_file_string = file_string.format(file_n,round2,sci_d2,flt_sci3)
print(new_file_string)
"""String Formatting lesson 3 task2"""
width = 4
precision = 1
round2 = f"result: {round2:{width}.{precision}}"
sci_d2 = int(float(sci_d2))
flt_sci3 = float("{:.2f}".format(float(flt_sci3)))
print(f"File index:{file_n} , {round2} , {sci_d2}, {flt_sci3}")
"""String formatting lesson 3 task 3"""












