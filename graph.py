import matplotlib.pyplot as plt
import seaborn as sns

def graph(x, y):
	sns.set_theme()
	sns.scatterplot(x=x, y=y)
	plt.show()