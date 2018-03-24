from mailroom import response_func

def test_response_func1():
	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Hulk':[10],'Spiderman':[40,20],'Superman':[40,60,10]}
	response_func(donors, 'Antman',10)
	assert donors['Antman'] == [10]

def test_response_func2():
	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Hulk':[10],'Spiderman':[40,20],'Superman':[40,60,10]}
	response_func(donors, 'Batman',10)
	assert donors['Batman'] == [100,50,30,10]