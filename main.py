import requests

if __name__ == '__main__':
	print(requests.get('https://coagmet.colostate.edu/data/daily.json?from=1991-01-01&to=now&fields=tMax').text)