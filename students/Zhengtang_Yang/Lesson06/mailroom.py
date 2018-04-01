from cursesmenu import SelectionMenu

def first_selection(res):
	response = input("Enter a Full Name or 'list' to see donor\n")
	while response == 'list':
		for item in res.keys():
			print(item)
		response = input("Enter a Full Name or 'list' to see donor\n")
	else:
		d_amount = input("Enter a donation amount\n")
		response_func(res, response, d_amount)
		print(response + ', thank you for your donation.')
		input("Press Enter to continue...")

def response_func(res, response, d_amount):
	try:
		if response in res:
			res[response].append(int(d_amount))
		else:
			res[response] = [int(d_amount)]
	except ValueError:
		print("Please Enter a number.")
		input("Press Enter to continue...")

def second_selection(res):
	header = ('Donor Name','Total Given','Num Gifts','Average Gift')
	row_format, row_format0 = '{:<14}','{:<14}'
	for item in header[1:]:
		row_format += f' | {{:>{len(item)}}}'
		row_format0 += f'  {{}}{{:>{len(item)}}}'
	print(row_format.format(*header))
	print('-'*len(row_format.format(*header)))
	for item in res.keys():
		print(row_format0.format(item,'$',sum(res[item]),' ',len(res[item]),'$',round(sum(res[item])/len(res[item]),1)))
	input("Press Enter to continue...") 

def third_selection(res):
	for names in res.keys():
		with open(f'{names}.txt','w') as text_file:
			print(f'Dear {names},\nThank you for your very kind donation of ${sum(res[names])}.\nIt will be put to very good use.\nSincerely,\n-The Team', file=text_file)

if __name__ == "__main__":
	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Hulk':[10],'Spiderman':[40,20],'Superman':[40,60,10]}
	a_list = ['Send a Thank You','Create a Report','Send letters to everyone']
	selection_dict = {0: first_selection, 1: second_selection, 2: third_selection}
	while True: 
		selection = SelectionMenu.get_selection(a_list)
		if selection == 3:
			break
		selection_dict.get(selection)(donors)