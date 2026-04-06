import requests
import pandas as pd

def getAsDF():
	url = "https://coagmet.colostate.edu/data/nw/daily/bld02.json?from=start&to=now&fields=tMax"

	data = requests.get(url).json()

	dates = []
	temps = []

	for d, t in zip(data["time"], data["tMax"]):
		dates.append(d)
		temps.append(t)

	return pd.DataFrame({'time': dates, 'temps': temps})