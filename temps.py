import requests
import pandas as pd

def getJsonAsDF():
	url = "https://coagmet.colostate.edu/data/nw/daily/bld02.json?from=start&to=now&fields=tMax"

	data = requests.get(url).json()

	dates = []
	temps = []

	for d, t in zip(data["time"], data["tMax"]):
		dates.append(d)
		temps.append(t)
		
	df = pd.DataFrame({'time': dates, 'temp': temps})

	return df

def getCsvAsDF():
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
