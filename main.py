import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

def graph(x, y):
	sns.set_theme()
	sns.scatterplot(x=x, y=y)
	plt.show()

if __name__ == '__main__':
	data = json.loads(requests.get('https://coagmet.colostate.edu/data/nw/daily/bld02.json?from=start&to=now&fields=tMax').text)
	print(data)
