import requests
import pandas as pd

def getData(fields=['tAvg','tMin','tMax']):
	url = f'https://coagmet.colostate.edu/data/nw/daily/bld02.json?from=start&to=now&fields={','.join(fields)}'
	
	# limit to desired fields
	data = pd.read_json(url)[['time'] + fields]

	# clean
	if 'tAvg' in fields: data = data[data['tAvg'] > -50]
	if 'tMin' in fields: data = data[data['tMin'] > -50]
	if 'tMax' in fields: data = data[data['tMax'] > -50]

	print(data)

	return data

def getDataCSV():
	url = "https://coagmet.colostate.edu/data/nw/daily/bld02.csv?from=start&to=now&fields=tMax"

	data = requests.get(url).text

	dates = []
	temps = []

	for line in data.split('\n'):
		split = line.strip().split(',')
		if len(split) > 2:
			dates.append(split[1].strip("\""))
			temps.append(float(split[2]))

	return pd.DataFrame({'time': dates, 'temp': temps})
