import matplotlib.pyplot as plt
import seaborn as sns

def graphDates(x, y):
	fig, ax = plt.subplots(figsize = (12,6))
	fig = sns.barplot(x=x, y=y, estimator=sum, ax=ax)
	x_dates = sorted(list(set(x)))
	ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
	plt.show()