import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

def graph(x, y):
	sns.set_theme()
	sns.scatterplot(x=x, y=y)
	plt.show()

if __name__ == '__main__':
	data = json.loads(requests.get('https://coagmet.colostate.edu/data/daily.json?from=1991-01-01&to=now&fields=tMax').text)
	print(data)