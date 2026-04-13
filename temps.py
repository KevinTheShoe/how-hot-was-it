import pandas as pd

def getData(fields=['tAvg','tMin','tMax']):
	url = f"https://coagmet.colostate.edu/data/nw/daily/bld01.json?dateFmt=iso&from=start&to=now&fields={','.join(fields)}"
	
	# pull data
	data = pd.read_json(url)

	# limit to desired fields
	data = data[['time'] + fields]

	# clean
	if 'tAvg' in fields: data = data[data['tAvg'] > -50]
	if 'tMin' in fields: data = data[data['tMin'] > -50]
	if 'tMax' in fields: data = data[data['tMax'] > -50]

	print(data)

	return data

def getDataCSV(fields=['tAvg','tMin','tMax']):
	url = f"https://coagmet.colostate.edu/data/nw/daily/bld01.csv?dateFmt=iso&from=start&to=now&fields={','.join(fields)}"
	
	# pull data
	data = pd.read_csv(url, header=None, names=['station id', 'time'] + fields)
	
	# limit to desired fields
	data = data[['time'] + fields]

	# clean
	if 'tAvg' in fields: data = data[data['tAvg'] > -50]
	if 'tMin' in fields: data = data[data['tMin'] > -50]
	if 'tMax' in fields: data = data[data['tMax'] > -50]

	print(data)

	return data