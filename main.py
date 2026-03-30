import requests
import json

def graphTemps():
	

if __name__ == '__main__':
	data = json.loads(requests.get('https://coagmet.colostate.edu/data/daily.json?from=1991-01-01&to=now&fields=tMax').text)
	print(data)