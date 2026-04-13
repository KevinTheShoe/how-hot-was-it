import pandas as pd

def getData(station, isNW, fields=['tAvg','tMin','tMax']):
	url = f"https://coagmet.colostate.edu/data/{'nw/' if isNW else ''}daily/{station}.json?dateFmt=iso&from=start&to=now&fields={','.join(fields)}"
	
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

def getAllStationDataCSV(fields=['tMax']):
	url = f"https://coagmet.colostate.edu/data/daily.csv?from=1991-01-01&to=now&dateFmt=iso&fields={','.join(fields)}"
	
	# pull data
	data = pd.read_csv(url, header=None, names=['sid', 'time'] + fields)
	
	# limit to desired fields
	data = data[['time'] + fields]

	# clean
	if 'tAvg' in fields: data = data[data['tAvg'] > -50]
	if 'tMin' in fields: data = data[data['tMin'] > -50]
	if 'tMax' in fields: data = data[data['tMax'] > -50]

	print(data)

	return data